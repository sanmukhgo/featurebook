from module import htag
from django.shortcuts import render, get_object_or_404
from .models import Heading
import sys
#sys.path.insert(0, '/path/to/featurebook/module')


def home(request):

    return render(request, 'toc/home.html', {})


def heading_list(request):

    Heading.objects.all().delete()

    heading_list = htag.headings()
    h=heading_list[1]
    for h in heading_list[1:]:
        Heading.objects.create(tag=h['tag'], text=h['text'])

    headings = Heading.objects.all()

    return render(request, 'toc/heading_list.html', {'headings': headings})
