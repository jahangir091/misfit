from django.db import models
from django.utils.translation import ugettext_lazy as _

from misfitproject.people.models import Profile
# Create your models here.

class UserRequest(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    owner = models.ForeignKey('people.Profile', related_name='owner', blank=True, null=True)
    last_auditor = models.ForeignKey('people.Profile', related_name='last_auditor', blank=True, null=True)
    status = models.CharField(max_length=10, choices=[
        ("OPEN", _("Open")),
        ("PROCESSED", _("Processed")),
        ("REVIEWED", _("Reviewed"))],
                              default="OPEN")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
