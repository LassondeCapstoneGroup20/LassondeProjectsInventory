from django.urls import path

from . import views

app_name = "faculty"
urlpatterns = [
    path('add/', views.add_edit_faculty, name='add'),
    path('', views.list, name='list'),
    path('<int:faculty_id>/delete', views.delete_faculty, name='delete'),
    path('<int:faculty_id>/details', views.details, name='details'),
    path('<int:faculty_id>/edit', views.add_edit_faculty, name='edit'),
]