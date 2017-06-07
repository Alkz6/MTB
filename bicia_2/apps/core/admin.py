from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from .forms import SuscriptionForm

#from ajax_select.fields import AutoCompleteSelectField

# Register your models here.

class EventAdmin(admin.ModelAdmin):

  list_display = ('name', 'date', 'cost', 'suscriptions', 'left_suscriptions', 'jerseys', 'left_jerseys', 'medals', 'left_medals')
  
  def get_form(self, request, obj=None, **kwargs):
    self.exclude = ('left_medals', 'left_jerseys', 'left_suscriptions')
    form = super(EventAdmin, self).get_form(request, obj, **kwargs)
    return form


class CyclistAdmin(admin.ModelAdmin):
  pass


"""
class SuscriptionAdmin(admin.ModelAdmin):

  list_display = ('event', 'cyclist', 'number', 'jersey', 'medal', 'ride', 'package', 'status')

  def get_form(self, request, obj=None, **kwargs):
    self.exclude = ('number', 'user')
    form = super(SuscriptionAdmin, self).get_form(request, obj, **kwargs)
    #import pdb; pdb.set_trace()
    form.fields['cyclist'] = AutoCompleteSelectField('cyclists')
    return form

  def save_model(self, request, obj, form, change):
  	obj.user = request.user
  	obj.save()
"""


class SuscriptionAdmin(admin.ModelAdmin):

  list_display = ('event', 'cyclist', 'number', 'jersey', 'medal', 'ride', 'package', 'status', 'user')

  form = SuscriptionForm

  def save_model(self, request, obj, form, change):
  	obj.user = request.user
  	obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(Cyclist, CyclistAdmin)
admin.site.register(Suscription, SuscriptionAdmin)
