from rest_framework import generics

from .models import Categoria, Autor, Livro
from .serializers import CategoriaSerializer, AutorSerializer, LivroSerializer
from .filters import CategoriaFilter, AutorFilter, LivroFilter

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    filterset_class = CategoriaFilter
    search_fields = ("^name",)
    ordering_fields = ("name",)
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = LivroSerializer
    name = "categoria-detail"
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "categoria-list"
    filterset_class = AutorFilter
    search_fields = ("^name",)
    ordering_fields = ("name",)
 
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-categoria"
   
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    name = "livro-list"
    filterset_fields = ("categoria", "autor")
    search_fields = ("^name",)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

  
        