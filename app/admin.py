__author__ = 'robert'
from django.contrib import admin
from models import *

admin.site.register(Location)
admin.site.register(Mine)
admin.site.register(Occupation)
admin.site.register(Employee)