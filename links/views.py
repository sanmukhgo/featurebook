from module import link
from django.shortcuts import render
from .models import Link


def link_list(request):

    Link.objects.all().delete()

    link_list = link.links('http')
    for l in link_list:
        Link.objects.create(url=l['url'], text=l['text'])

    links = Link.objects.all()

    return render(request, 'links/link_list.html', {'links': links})