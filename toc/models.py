from django.db import models
from django.conf import settings


class Heading(models.Model):

    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.CharField(max_length=10)
    text = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Heading")
        verbose_name_plural = ("Headings")

    def __str__(self):
        return self.text
