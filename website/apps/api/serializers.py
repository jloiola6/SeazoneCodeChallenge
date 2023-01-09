# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from apps.api.models import Imovel, Anuncio, Reserva
 
# Create a model serializer
class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Imovel
        fields = ('__all__')


class AnuncioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anuncio
        fields = ('__all__')


class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')
        read_only_fields = ('codigo',)