from django.urls import path
from . import views

app_name = 'toc'

urlpatterns = [
    ### All URL prefixed by toc/ ###
    
    path('', views.heading_list, name='heading_list'),
]
