from django.urls import path

from . import views

app_name = "capstones"
urlpatterns = [
  path('add/', views.add_edit_capstone, name='add'),
  path('list/', views.list, name='list'),
  path('delete/<int:year>/', views.delete_capstone, name='delete'),
]