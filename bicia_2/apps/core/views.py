from django.shortcuts import render

# Create your views here.
from dal import autocomplete
from .models import Cyclist
from django.db.models import Q


class CyclistAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cyclist.objects.none()

        qs = Cyclist.objects.all()
        if self.q:
            qs = qs.filter( Q(firstname__icontains=self.q) | Q(lastname__icontains=self.q) | Q(secondlastname__icontains=self.q) | Q(nickname__icontains=self.q) )
        return qs