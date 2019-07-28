from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    info = models.TextField(default='info')
    branding = models.CharField(max_length=255, default='branding')

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Settings"