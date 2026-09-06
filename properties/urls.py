from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.PropertyListView.as_view(), name='property_list'),
    path('properties/<slug:slug>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 