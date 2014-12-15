from django.db import models


#Students model
class Student(models.Model):
    PACKAGE_CHOICES = (('s', 'Standard'),
                       ('g', 'Gold'),
                       ('p', 'Platinum'))
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, blank=True)
    courses = models.ManyToManyField('courses.Course', blank=True, null=True)
    package = models.CharField(max_length=1, choices=PACKAGE_CHOICES,
                               default='s')
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)


    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


#Dossier model
class Dossier(models.Model):
    COLORS = (('r', 'Red'),
              ('o', 'Orange'),
              ('y', 'Yellow'),
              ('g', 'Green'),
              ('l', 'Light Blue'),
              ('b', 'Blue'),
              ('v', 'Violet'),)

    address = models.ForeignKey('students.Address', blank=True, null=True)
    unliked_courses = models.ManyToManyField('courses.Course', blank=True, null=True)
    favourite_color = models.CharField(max_length=1, choices=COLORS, default='r', blank=True)

    def __unicode__(self):
        return "Dossier %d" % self.id


#Address model
class Address(models.Model):
    zip = models.CharField(max_length=5)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s %s, %s, %s %s" % (self.zip, self.country.upper(), self.city, self.street, self.house)