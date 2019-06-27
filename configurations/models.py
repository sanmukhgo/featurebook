from django.db import models
from django.conf import settings

class ConfigTable(models.Model):

    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    source = models.TextField()
    configuration = models.TextField()
    description = models.TextField()
    values = models.TextField()
    default = models.TextField()

    class Meta:
        verbose_name = ("ConfigurationTable")
        verbose_name_plural = ("ConfigurationTables")

    def __str__(self):
        return self.source


