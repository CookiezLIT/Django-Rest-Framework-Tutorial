from rest_framework import serializers


class AngajatSerializer(serializers.Serializer):

    nume = serializers.CharField(max_length=250)
    prenume = serializers.CharField(max_length=250)
    varsta = serializers.IntegerField()
    oras = serializers.CharField(max_length=250)



