from models import Angajat
from serializers import AngajatSerializer
from rest_framework import generics


class AngajatList(generics.GenericAPIView):
    queryset = Angajat.objects.all()
    serializer_class = AngajatSerializer


