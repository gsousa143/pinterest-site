
from django.urls import path
from . import views

urlpatterns = [
    path("imagem/",views.imagem),
    path("imagem/<id>",views.imagem_id),
    path("tema/",views.GetPostTemaView.as_view()),
    path("tema/<id>",views.GetPutDeleteTemaView.as_view())
]
