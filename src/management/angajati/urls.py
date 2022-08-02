from django.urls import path
from angajati.views import AngajatList

urlpatterns = [
    path('toti_angajatii/', AngajatList.as_view()),
]
