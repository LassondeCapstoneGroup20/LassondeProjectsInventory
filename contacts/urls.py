from django.urls import path

from . import views

app_name = "contacts"
urlpatterns = [
    path('add/', views.add_industry_partner, name='add'),
    path('list/', views.list, name='list'),
    path('success/', views.success, name='success'),
    path('delete/<int:partner_id>/', views.delete_partner, name='delete'),
    path('edit/<int:partner_id>/', views.edit_partner, name='edit'),

]