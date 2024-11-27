from django.urls import path
from . import views

urlpatterns = [
     # path('livros/', views.LivroList.as_view(), name='livros-list'),
     # path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),

     path("categoria/", 
          views.CategoriaList.as_view(),
          name=views.CategoriaList.name),
     path("categoria/<int:pk>/",
          views.CategoriaDetail.as_view(),
          name=views.CategoriaDetail.name),
     path("autor/",
          views.AutorList.as_view(),
          name=views.AutorList.name),
     path("autor/<int:pk>/",
          views.AutorDetail.as_view(),
          name=views.AutorDetail.name),
     path("livro/",
          views.LivroList.as_view(),
          name=views.LivroList.name),
     path("livro/<int:pk>/",
          views.LivroDetail.as_view(),
          name=views.LivroDetail.name),
     path("colecao/",
          views.ColecaoListCreate.as_view(),
          name=views.ColecaoListCreate.name),
     path("colecao/<int:pk>",
          views.ColecaoDetail.as_view(),
          name=views.ColecaoDetail.name),
]