from django.db import models


# Create your models here.
class SaveUrl(models.Model):
    url = models.CharField(max_length=255)


class Results(models.Model):
    base_url = models.CharField(default=True, max_length=255, blank=True)
    url = models.CharField(default=True, max_length=255, blank=True)
    title = models.CharField(default=True, max_length=255, blank=True)
    description = models.CharField(default=True, max_length=255, blank=True)
    title_unique = models.CharField(default=True, max_length=255, blank=True)
    description_unique = models.CharField(default=True, max_length=255, blank=True)
    keywords = models.CharField(default=True, max_length=255, blank=True)
    yandex = models.CharField(default=True, max_length=255, blank=True)
    google = models.CharField(default=True, max_length=255, blank=True)
    h1 = models.CharField(default=True, max_length=255, blank=True)
    h2 = models.CharField(default=True, max_length=255, blank=True)
    vk = models.CharField(default=True, max_length=255, blank=True)
    facebook = models.CharField(default=True, max_length=255, blank=True)
    instagram = models.CharField(default=True, max_length=255, blank=True)
    broken_link = models.CharField(default=True, max_length=255,blank=True)
    date_add = models.DateField(auto_now_add=True)


class DeleteWhileSaving(models.Model):
    title = models.CharField(max_length=255)
    keyrwords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
