from django.shortcuts import render
from module import reqpage
from configurations.views import create_config_table
from links.views import create_link_list
from toc.views import create_heading_list


def home(request):

    return render(request, 'home/homepage.html', {})


def reload_(request):

    render(request, 'home/loading.html', {})

    reqpage.save_inventory()
    create_config_table()
    create_heading_list()
    create_link_list()

    return home(request)