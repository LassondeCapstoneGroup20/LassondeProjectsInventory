from django.urls import path

from . import views

app_name = "capstones"
urlpatterns = [
  path('add/', views.add_edit_capstone, name='add'),
  path('', views.list, name='list'),
  path('<int:year>/delete', views.delete_capstone, name='delete'),
  path('<int:year>/edit', views.add_edit_capstone, name='edit'),
  path('<int:year>/details', views.details, name='details'),
  path('<int:year>/award', views.add_award, name='add_award'),
  path('<int:year>/award/<int:id>', views.add_award, name='edit_award'),
  path('<int:year>/award/<int:id>/delete', views.delete_award, name='delete_award'),
]