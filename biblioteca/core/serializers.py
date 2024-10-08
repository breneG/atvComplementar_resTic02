from rest_framework import serializers 
from core.models import Categoria, Autor, Livro

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = "livro-detail"
    )
    
    class Meta:
        model = Categoria
        fields = ("nome")
        
class AutorSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = "livro-detail"
    )
    
    class Meta:
        model = Autor
        fields = ("nome")
        
class LivroSerializer(serializers.HyperlinkedModelSerializer):
    categoria = serializers.SlugRelatedField(
        queryset = Categoria.objects.all(), slug_field = "name"
    )
    autor = serializers.SlugRelatedField(
        queryset = Autor.objects.all(), slug_field = "name"
    )
    
    class Meta:
        fields = (
            "titulo",
            "autor",
            "categoria",
            "publicado_em"
        )

 
