from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_project, name='add'),
    path('success/', views.success, name='success'),
    path('delete/', views.delete_project, name='delete'),
]