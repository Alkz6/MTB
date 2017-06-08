from django.shortcuts import render

# Create your views here.
from dal import autocomplete
from .models import Cyclist
from django.db.models import Q
from django.http import Http404 
from django.http import HttpResponseRedirect
from .models import Suscription
from django.http import JsonResponse


class CyclistAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cyclist.objects.none()

        qs = Cyclist.objects.all()
        if self.q:
            qs = qs.filter( Q(firstname__icontains=self.q) | Q(lastname__icontains=self.q) | Q(secondlastname__icontains=self.q) | Q(nickname__icontains=self.q) )
        return qs


def home(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect('/admin/')
  return render(request, 'base.html')


def records(request):
  if request.is_ajax():
    try:
      list_suscriptions =  Suscription.objects.all()
      total = list_suscriptions.count()
      list_result = []
      for suscription in list_suscriptions:
        list_result.append({
          'cyclist': suscription.cyclist.__str__(),
          'number': suscription.number,
          'jersey': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.jersey else '<i class="fa fa-times" aria-hidden="true"></i>',
          'medal': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.medal else '<i class="fa fa-times" aria-hidden="true"></i>',
          'ride': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.ride else '<i class="fa fa-times" aria-hidden="true"></i>',
          'package': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.package == 'D' else '<i class="fa fa-times" aria-hidden="true"></i>',
          'status': '<i class="fa fa-check" aria-hidden="true"></i>' if suscription.status == 'A' else '<i class="fa fa-times" aria-hidden="true"></i>',
          'register': suscription.user.__str__(),
        })
      result = {
        'data': list_result,
        'iTotalRecords': total,
        'iTotalDisplayRecords': total,
        'aiDisplay': total,
        'aiDisplayMaster': total,
        '_iRecordsDisplay': total,
      }
      print result
      return JsonResponse(result)
    except Exception, e:
      print str(e)
      raise Http404