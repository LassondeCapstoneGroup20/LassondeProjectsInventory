from django.urls import path

from . import views

app_name = "contacts"
urlpatterns = [
    path('add/', views.add_industry_parnter, name='add'),
    path('list/', views.list, name='list'),
    path('success/', views.success, name='success')
]