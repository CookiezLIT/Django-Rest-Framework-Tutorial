from angajati.models import Angajat
from angajati.serializers import AngajatSerializer
from rest_framework import generics


class AngajatList(generics.ListCreateAPIView):
    queryset = Angajat.objects.all()
    serializer_class = AngajatSerializer
    permission_classes = []
