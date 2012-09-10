#-*- coding: gb2312 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Location(models.Model):
    name = models.CharField(_(u"����"), max_length=40, primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    #slug = models.SlugField(max_length=40)
    comment = models.CharField(_(u"��ע"), max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Mine(models.Model):
    name =  models.CharField(_(u"����"), max_length=20, blank=False, null=False, unique=True)
    sn = models.CharField(_(u"�����"), max_length=20, primary_key=True, blank=False)
    location = models.ForeignKey('Location')
    #slug = models.SlugField(max_length=40)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-sn',]

class Occupation(models.Model):
    name = models.CharField(_(u"ְ������"), max_length=20, blank=False, null=False, unique=True)
    comment =  models.CharField(_(u"��ע"),max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    name =  models.CharField(_(u"����"), max_length=20, blank=False, null=False)
    sn = models.CharField(_(u"�����"),max_length=20, primary_key=True)
    #occupation = models.ForeignKey('Occupation')
    occupation = models.CharField(_(u"����"), max_length=20, blank=False, null=False)
    mine = models.ForeignKey('Mine', verbose_name=_(u"��id"))
    age = models.IntegerField(_(u"����"), max_length=2)
    gender = models.BooleanField(_(u"�Ա�"), default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'sn', 'mine']

class Area(models.Model):
    sn = models.CharField(_(u"�����"), max_length=20, primary_key=True)
    mine = models.ForeignKey('Mine')
    num = models.IntegerField(max_length=5)
    name = models.CharField(_(u"��������"), max_length=20, null=False, blank=False)
    describe = models.CharField(_(u"��������"), max_length=20, null=False, default=u"��������")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['sn', 'mine']

class Point(models.Model):
    sn = models.CharField(_(u"̽�������"), max_length=20, primary_key=True)
    mine = models.ForeignKey('Mine')
    name = models.CharField(_(u"̽����λ������"), max_length=20, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def Meta(self):
        ordering = ['sn', 'mine']

class LocationReal(models.Model):
    sn = models.ForeignKey('Employee')
    mine = models.ForeignKey('Mine')
    area = models.ForeignKey('Area')
    point = models.ForeignKey('Point')
    current_time = models.DateTimeField()




