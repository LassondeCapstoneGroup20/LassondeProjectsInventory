from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

import os

from pathlib import Path

from .forms import DisciplineForm, GoalForm, ProjectForm, ProjectsImportForm
from .filters import ProjectFilter
from .models import EngDiscipline, Project, UNGoals

from authentication.views import login_required, loginUser
from googleapiclient.http import MediaFileUpload
import projects.google_apis as google_api


import pandas as pd
from datetime import datetime

@login_required(login_url=loginUser)
def project_index_page(request):
    return render(request, 'projects/index.html')

@login_required(login_url=loginUser)
def list(request):
    project_filter = ProjectFilter(request.GET, queryset = Project.objects.all())
    context = {'filter_form': project_filter.form, 'project_list': project_filter.qs}
    return render(request, 'projects/list.html', context)

@login_required(login_url=loginUser)
def detail(request, proj_id):
    proj = get_object_or_404(Project, id=proj_id)
    return render(request, 'projects/detail.html', {'proj': proj})

@login_required(login_url=loginUser)
def delete_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    if request.method == "POST":
        proj.delete()
    return HttpResponseRedirect('/projects/list/')

@login_required(login_url=loginUser)
def add_edit_project(request, proj_id = None):
    if proj_id:
        proj = get_object_or_404(Project, id = proj_id)
        print(request.FILES)
        form = ProjectForm(request.POST or None, request.FILES if len(request.FILES)>0 else None, instance=proj)
    else:
        form = ProjectForm(request.POST or None, request.FILES if len(request.FILES)>0 else None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            if form.is_valid():
                instance = form.instance
                check_add_form_video = proj_id==None and instance.file_capstone is not None and str(instance.file_capstone)!=''
                check_edit_form_video = proj_id!=None and instance.file_capstone is not None and "https://www.youtube.com/watch?v=" not in str(instance.file_capstone) and str(instance.file_capstone)!=''
                if check_add_form_video or check_edit_form_video:
                    print(instance.file_capstone)
                    print(type(instance.file_capstone))
                    local_path = str(instance.file_capstone)
                    try:
                        video_id = upload_video(instance.name + ' ' + str(instance.capstone_year) + ' ' + str(instance.students) + ' Capstone video', str(instance.file_capstone))
                        os.remove(local_path)
                        instance.file_capstone = "https://www.youtube.com/watch?v=" + str(video_id)
                    except Exception as e:
                        print(e)
                        print("Could not upload video to youtube or could not remove from filepath. Please check quota and logs.")
                    form.save()
            return HttpResponseRedirect('/projects/list/')
    return render(request, 'projects/add.html', {'form': form})

@login_required(login_url=loginUser)
def bulk_import(request):
    if request.method == "POST":
        form = ProjectsImportForm(request.POST, request.FILES)
        ef = request.FILES["file"]
        df = pd.read_excel(ef)
        #df = df.reset_index()
        df_cleaned = __clean_df(df).to_dict('records')
        print(df_cleaned)
        p = __to_models(df_cleaned)
        #print(p)
        Project.objects.bulk_create(p)
        return HttpResponseRedirect('/projects/list/')
    else:
        form = ProjectsImportForm()
    return render(request, 'projects/import.html', {'form': form})

@login_required(login_url=loginUser)
def settings(request):
    eng_disciplines = EngDiscipline.objects.order_by('id')[:15]
    un_goals = UNGoals.objects.order_by('id')[:18]
    context = {'disciplines': eng_disciplines, 'goals':un_goals}
    return render(request, 'projects/settings.html', context)

@login_required(login_url=loginUser)
def add_discipline(request, id=None):
    if id:
        disc = get_object_or_404(EngDiscipline, id=id)
        form = DisciplineForm(request.POST or None, instance=disc)
    else:
        form = DisciplineForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/settings')
    return render(request, 'projects/add_discipline.html', {'form': form})

@login_required(login_url=loginUser)
def delete_discipline(request, id):
    disc = get_object_or_404(EngDiscipline, id=id)
    if request.method == "POST":
        disc.delete()
    return HttpResponseRedirect('/projects/settings')

@login_required(login_url=loginUser)
def add_goal(request, id=None):
    if id:
        goal = get_object_or_404(UNGoals, id=id)
        form = GoalForm(request.POST or None, instance=goal)
    else:
        form = GoalForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/settings')
    return render(request, 'projects/add_sdg.html', {'form': form})

@login_required(login_url=loginUser)
def delete_goal(request, id):
    goal = get_object_or_404(UNGoals, id=id)
    if request.method == "POST":
        goal.delete()
    return HttpResponseRedirect('/projects/settings')

'''Helper Methods'''
def __save_form(form, redir):
    if form.is_valid():
        print("Success")
        form.save()
        return redirect(redir)
    
def upload_video(title, video_location):
    # Initiate instance
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    client_file = 'client_secrets.json'
    BASE_DIR = Path(__file__).resolve().parent.parent
    client_file = os.path.join(BASE_DIR, client_file)
    service = google_api.create_service(client_file, API_NAME, API_VERSION, SCOPES)
    print(title)
    # Make upload details
    upload_time = (datetime.now()).isoformat() + '.000Z'
    request_body = {
        'snippet': {
            'title': title,
            'description': 'This is the video for ' + title,
            'categoryId': 27,
            'tags': ['Capstone Video']
        },
        'status': {
            'privacyStatus': 'private',
            'publishedAt': upload_time,
            'selfDeclaredMadeForKids': False
        },
        'notifySubscribers': False
    }

    video_file = os.path.join(BASE_DIR, video_location)
    print(video_file)
    media_file = MediaFileUpload(video_file)

    response_video_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()
    return response_video_upload.get('id')

def generate_unique_file_name(f):
    file_path= 'projects/static/upload/'
    # Generate a timestamp with microsecond precision
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    # Append the timestamp to the file name and re-add the extension
    new_file_name = f"{file_path}/{timestamp}-{f.name}"
    return new_file_name

def upload_files(f, oldfilename):
    filename_old = "projects/static/upload/" + oldfilename
    file_path_name = generate_unique_file_name(f)

    if os.path.isfile(oldfilename):
       os.remove(filename_old)

    with open(file_path_name, 'wb+') as des:
        for c in f.chunks():
            des.write(c)

def __clean_df(df):
    df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
    del df['First Name']
    del df['Last Name']
    agg_functions = {'Project Title': 'unique', 'Project Discipline': 'unique', 'Supervisor': 'unique', 'Year': 'unique', 'Full Name': 'unique'}
    if 'Email Address' in df.columns:
        del df['Email Address']
    if 'Discipline' in df.columns:
        del df['Discipline']
    if 'Supervisor Email' in df.columns:
        del df['Supervisor Email']
    if 'Date Proposed' in df.columns:
        df['Date Proposed'] = df['Date Proposed'].dt.strftime('%Y-%m-%d')
        agg_functions.update({'Date Proposed': 'unique'})
    if 'Date Complete' in df.columns:
        df['Date Complete'] = df['Date Complete'].dt.strftime('%Y-%m-%d')
        agg_functions.update({'Date Complete': 'unique'})
    if 'Type' in df.columns:
        agg_functions.update({'Type': 'unique'})
    df = df.applymap(str)         
    
    return df.groupby(['Team'], as_index=False).agg(agg_functions)

def __to_models(proj_list):
    projects = []
    for p in proj_list:
        year = int(p['Year'][0])
        projects.append(Project(
            name = p['Project Title'][0],
            capstone_year = year,
            type=p.get('Type', ['COMP'])[0],
            students = ', '.join(p['Full Name']),
            status='COMPL',
            date_proposed = datetime.strptime(p.get('Date Proposed', [str(year)+'-1-1'])[0], '%Y-%m-%d'),
            date_complete = datetime.strptime(p.get('Date Complete', [str(year+1)+'-4-30'])[0], '%Y-%m-%d'),
            #Todo: set the discipline, project supervisor
        )
    )
    return projects

# Create your views here.
