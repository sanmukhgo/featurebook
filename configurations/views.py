from django.shortcuts import render
from module import configtable
from .models import ConfigTable


def create_config_table():

    ConfigTable.objects.all().delete()

    table = configtable.get_configtable()
    length = len(table['Source'])

    for i in range(length):
        ConfigTable.objects.create(source=table['Source'][i],
                                   configuration=table['Configuration'][i],
                                   description=table['Description'][i],
                                   values=table['Values'][i],
                                   default=table['Default'][i])


def config_table(request):

    if ConfigTable.objects.all().count() == 0:
        create_config_table()

    ctable = ConfigTable.objects.all()
    return render(request, 'configurations/config_table.html', {'ctable': ctable})
