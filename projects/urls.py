from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.project_index_page, name='index'),
    path('list/', views.list, name='list'),
    path('list/<int:proj_id>/', views.detail, name='detail'),
    path('add/', views.add_edit_project, name='add'),
    path('import/', views.bulk_import, name='bulk_import'),
    path('edit/<int:proj_id>', views.add_edit_project, name='edit'),
    path('delete/<int:proj_id>/', views.delete_project, name='delete'),
    path('settings/', views.settings, name = 'settings'),
    path('settings/add_discipline/',views.add_discipline, name = 'add_discipline'),
    path('setting/add_goal', views.add_goal, name='add_goal'),
]