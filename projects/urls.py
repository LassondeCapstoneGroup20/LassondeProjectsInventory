from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('list/<int:proj_id>/', views.detail, name='detail'),
    path('add/', views.add_project, name='add'),
    path('success/', views.success, name='success'),
    path('delete/', views.delete_project, name='delete'),
]