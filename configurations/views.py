from django.shortcuts import render
from module import configtable
from .models import ConfigTable


def config_table(request):

    ConfigTable.objects.all().delete()

    table = configtable.get_configtable()
    length = len(table['Source'])

    for i in range(length):
        ConfigTable.objects.create(source=table['Source'][i],
                                   configuration=table['Configuration'][i],
                                   description=table['Description'][i],
                                   values=table['Values'][i],
                                   default=table['Default'][i])
    ctable = ConfigTable.objects.all()

    return render(request, 'configurations/config_table.html', {'ctable': ctable})
