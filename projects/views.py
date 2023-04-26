from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

import os

from pathlib import Path

from .forms import DisciplineForm, GoalForm, ProjectForm
from .filters import ProjectFilter
from .models import EngDiscipline, Project, UNGoals

from authentication.views import login_required, loginUser
import datetime
from googleapiclient.http import MediaFileUpload
import projects.google_apis as google_api


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
def settings(request):
    eng_disciplines = EngDiscipline.objects.order_by('id')[:15]
    un_goals = UNGoals.objects.order_by('id')[:18]
    context = {'disciplines': eng_disciplines, 'goals':un_goals}
    return render(request, 'projects/settings.html', context)

@login_required(login_url=loginUser)
def add_discipline(request):
    if request.method == "POST":
        return __save_form(DisciplineForm(request.POST), 'projects:settings')
    form = DisciplineForm()
    return render(request, 'projects/add_settings.html', {'form': form})

@login_required(login_url=loginUser)
def add_goal(request):
    #return HttpResponse('Add Goal')
    if request.method == "POST":
        return __save_form(GoalForm(request.POST), 'projects:settings')
    form = GoalForm()
    return render(request, 'projects/add_settings.html', {'form': form})


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
    upload_time = (datetime.datetime.now()).isoformat() + '.000Z'
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
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
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
