from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Sensores , Ambientes , Historico
from .serializers import SensoresSerializer , AmbientesSerializer , HistoricoSerializer
from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .utils import ler_excel, exportar_excel

# Listar Todos e criar sensores
class SensoresListCreate(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]
    

# Class que ira deletar, visualizar um em expecifico  e atualizar sensores
class  SensoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    #mensagem de erro quando o sensor não é encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Esse sensor não foi encontrado.")
        
    # mesnsagem de erro quando o sensor é excluido com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"O sensor foi excluído"})

# Listar Todos e criar ambientes
class AmbientesListCreate(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

# Class que ira deletar, visualizar um em expecifico  e atualizar ambientes
class AmbientesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    
    #mensagem de erro quando o ambiente não é encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Esse ambiente não foi encontrado.")
        
    # mesnsagem de erro quando o ambiente é excluido com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"O ambiente foi excluído"})

# Listar Todos e criar historico
class HistoricoListCreate(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]

# Class que ira deletar, visualizar um em expecifico  e atualizar Historico
class HistoricoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    #mensagem de erro quando o historico não é encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Esse historico não foi encontrado.")
        
    # mesnsagem de erro quando o historico é excluido com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"O historico foi excluído"})