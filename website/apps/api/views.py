from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from random import randint

from apps.api.serializers import *
 
# create a viewset
class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = ImovelSerializer
    queryset = Imovel.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['codigo', 'limite_hospedes', 'qtd_banheiros', 'aceita_animais', 'valor_limpeza', 'criacao', 'ultima_atualizacao']
    search_fields = ['codigo', 'limite_hospedes', 'qtd_banheiros', 'aceita_animais', 'valor_limpeza', 'criacao', 'ultima_atualizacao']

    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'put', 'delete']


class AnuncioViewSet(viewsets.ModelViewSet):
    serializer_class = AnuncioSerializer
    queryset = Anuncio.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = ['imovel', 'plataforma', 'taxa_plataforma', 'criacao', 'ultima_atualizacao']
    search_fields = ['imovel', 'plataforma', 'taxa_plataforma', 'criacao', 'ultima_atualizacao']

    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'put']


class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['codigo', 'anuncio', 'check_in', 'check_out', 'total', 'comentario', 'comentario', 'criacao', 'ultima_atualizacao']
    search_fields = ['codigo', 'anuncio', 'check_in', 'check_out', 'total', 'comentario', 'comentario', 'criacao', 'ultima_atualizacao']

    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        check_in = datetime.strptime(request.data['check_in'], '%Y-%m-%d').date()
        check_out = datetime.strptime(request.data['check_out'], '%Y-%m-%d').date()


        if check_in < check_out:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        content = {'erro': 'Data do checkin é posterior a de chekout'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

