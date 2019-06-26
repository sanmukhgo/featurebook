from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    ### All URLs prefixed by links/ ###
    
    path('', views.link_list, name='link_list'),
]
