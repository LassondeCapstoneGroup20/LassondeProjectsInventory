from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import EngDiscipline, Project

import pdb

# Create your tests here.
def create_project(
    proj_name = 'Default Test Name', 
    proj_type = Project.TYPES[0][0], 
    source = '', 
    students = '',
    supervisor = '',
    date_proposed = '2023-02-02',
    status = Project.STATUS[0][0],
    date_complete = '2023-02-02',
    industry_partners = '',
    cost = 0,
    un_goals = '',
    notes = '',
    ):
    return Project.objects.create(
        name = proj_name, 
        type = proj_type,
        source = source,
        students = students,
        supervisor = supervisor,
        date_proposed = date_proposed,
        status = status,
        date_complete = date_complete,
        industry_partners = industry_partners,
        cost = cost,
        notes = notes,
        )

class ProjectsListViewTests(TestCase):
    def test_no_projects(self):
        response = self.client.get(reverse('projects:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects available.")
        self.assertQuerysetEqual(response.context['project_list'], [])

    def test_one_project(self):
        proj_name = "Test Project Name"
        proj_field = 'Computer'
        proj_type = Project.TYPES[0][0]
        
        proj = create_project(proj_name = proj_name, proj_discipline = proj_field, proj_type = proj_type)
        #ed = EngDiscipline.objects.create(discipline = 'Test Discipline')
        #proj.discipline.add(ed)
        
        response = self.client.get(reverse('projects:list'))
        self.assertEqual(response.status_code, 200)
        #pdb.set_trace()
        self.assertQuerysetEqual(response.context['project_list'], [proj])
        
        returned_proj = response.context['project_list'].first()
        self.assertEqual(returned_proj.name, proj_name)
        self.assertEqual(returned_proj.type, proj_type)