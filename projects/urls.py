from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('list/<int:proj_id>/', views.detail, name='detail'),
    path('add/', views.add_project, name='add'),
    path('edit/<int:proj_id>', views.edit_project, name='edit'),
    path('success/', views.success, name='success'),
    path('delete/<int:proj_id>/', views.delete_project, name='delete'),
    path('settings/', views.settings, name = 'settings'),
    path('settings/add_discipline/',views.add_discipline, name = 'add_discipline'),
    path('setting/add_goal', views.add_goal, name='add_goal'),
]