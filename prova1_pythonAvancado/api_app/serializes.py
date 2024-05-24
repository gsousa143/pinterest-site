from rest_framework import serializers
from app.models import *

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ["id","titulo","imagem","tema"]


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = ["id","titulo"]