from module import htag
from django.shortcuts import render, get_object_or_404
from .models import Heading


def heading_list(request):

    Heading.objects.all().delete()

    heading_list = htag.headings()
    for h in heading_list[1:]:
        Heading.objects.create(tag=h['tag'], text=h['text'])

    headings = Heading.objects.all()

    return render(request, 'toc/heading_list.html', {'headings': headings})
