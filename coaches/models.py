from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Coach(models.Model):
    COACH_TYPES = (('C', 'Coach'), ('A', 'Assistant'))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, blank=True)
    type = models.CharField(choices=COACH_TYPES, max_length=1)
    user = models.ForeignKey(User, blank=True, null=True)
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.type)