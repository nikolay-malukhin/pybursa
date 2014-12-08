from django.db import models

# Create your models here.
from coaches.models import Coach


class Course(models.Model):
    TECHNOLOGY_CHOICE = (('p', 'Python'),
                         ('r', 'Ruby'),
                         ('j', "JavaScript"))
    name = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach)
    assistant = models.ForeignKey(Coach, blank=True,
                                  related_name="course_assistant")
    start_date = models.DateField()
    end_date = models.DateField()
    technology = models.CharField(max_length=255, choices=TECHNOLOGY_CHOICE)

    def __str__(self):
        return "%s (%s) - %s" % (self.name, self.coach, self.technology)