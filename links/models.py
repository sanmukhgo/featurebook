from django.db import models
from django.conf import settings


class Link(models.Model):

    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name = ("Link")
        verbose_name_plural = ("Links")

    def show_link(self):
        if self.text == '':
            return self.url
        else:
            return self.text

    def __str__(self):
        return self.text
