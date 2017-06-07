from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
  pass

class CyclistAdmin(admin.ModelAdmin):
  pass

class SuscriptionAdmin(admin.ModelAdmin):
  
  readonly_fields = ['user', ]

  def get_form(self, request, obj=None, **kwargs):
    self.exclude = ('number',)
    form = super(SuscriptionAdmin, self).get_form(request, obj, **kwargs)
    return form

  def get_changeform_initial_data(self, request):
    return {'user': request.user}



admin.site.register(Event, EventAdmin)
admin.site.register(Cyclist, CyclistAdmin)
admin.site.register(Suscription, SuscriptionAdmin)
