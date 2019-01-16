from django.db import models


class Group(models.Model):
    nazwa_grupy = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_grupy

    def __uncode__(self):
        return unicode(self.nazwa_grupy)

    def get_absolute_url(self):
        return "/main/%s/" %(self.id)


class User(models.Model):
    name = models.CharField(max_length=100)
    grupy = models.ManyToManyField(Group, null=True, blank=True, related_name='group_set')

    def __str__(self):
        return self.name

    def __uncode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return "/main/%s/" %(self.id)
