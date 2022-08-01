from django.urls import path
from views import AngajatList

urlpatterns = [
    path('toti_angajatii/', AngajatList.as_view()),
]
