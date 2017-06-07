# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
  pass

class CyclistAdmin(admin.ModelAdmin):
  pass

class SuscriptionAdmin(admin.ModelAdmin):
  pass


admin.site.register(Event, EventAdmin)
admin.site.register(Cyclist, CyclistAdmin)
admin.site.register(Suscription, SuscriptionAdmin)

