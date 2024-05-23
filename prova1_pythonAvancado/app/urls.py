
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),

    path("add_imagem",views.add_imagem,name='add_imagem'),
    path("form_imagem",views.form_imagem,name="form_imagem"),

    path("perfil",views.perfil,name="perfil"),
    path("cadastro",views.cadastro,name="cadastro"),

    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    
    path("editar_perfil",views.editar_perfil,name="editar_perfil"),


    path('galeria', views.galeria,name="galeria"),

    path("add_galeria/<id>", views.add_galeria, name="add_galeria"),
    path("remover_galeria/<id>", views.remover_galeria, name="remover_galeria"),

]