from django.conf.urls import include, url
from .views import CyclistAutocomplete

urlpatterns = [
    url(
        r'^cyclist-autocomplete/$', CyclistAutocomplete.as_view(), name='cyclist-autocomplete',
    ),
]