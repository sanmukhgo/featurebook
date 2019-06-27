from module import link
from django.shortcuts import render
from .models import Link

def create_link_list():

    Link.objects.all().delete()

    link_list = link.links('http')
    for l in link_list:
        Link.objects.create(url=l['url'], text=l['text'])
		

def link_list(request):

    if Link.objects.all().count() == 0:
        create_link_list()

    links = Link.objects.all()
    return render(request, 'links/link_list.html', {'links': links})