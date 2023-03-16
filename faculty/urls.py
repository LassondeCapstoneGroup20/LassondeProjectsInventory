from django.urls import path

from . import views

app_name = "faculty"
urlpatterns = [
    path('add/', views.add_edit_faculty, name='add'),
    path('list/', views.list, name='list'),
    path('delete/<int:faculty_id>/', views.delete_faculty, name='delete'),

]