from django.urls import path
from . import views

app_name='configurations'

urlpatterns = [
    path('', views.config_table, name='config_table'),
]
