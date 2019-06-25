from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toc/', views.heading_list, name='heading_list'),
]
