from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from app.models import Imagem
from .serializes import *
from rest_framework.response import Response
# Create your views here.



#METODO COM DECORATORS
@api_view(["GET","POST"])
def imagem(request):
    if request.method == "POST":
        serializer = ImagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    elif request.method == "GET":
        imagens = Imagem.objects.all()
        serializer = ImagemSerializer(imagens,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["GET","PUT","DELETE"])
def imagem_id(request,id):
    try:
        imagem = Imagem.objects.get(id=id)
    except Imagem.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ImagemSerializer(imagem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ImagemSerializer(instance=imagem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        imagem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#METODO UTILIZANDO CLASSES
class GetPostTemaView(APIView):
    def get(self,request):
        if request.user.is_autheticated:
            temas = Tema.objects.all()
            serializer = TemaSerializer(temas,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

    def post(self,request):
        if request.user.is_autheticated and request.user.is_superuser:
            serializer = TemaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class GetPutDeleteTemaView(APIView):
    def get_object(self,request,id):
        try:
            tema = Tema.objects.get(id=id)
            return tema
        except Tema.DoesNotExist:
            raise NotFound()

    def get(self,request,id):
        if request.user.is_autheticated:
            tema = self.get_object(request,id)
            serializer = TemaSerializer(tema)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self,request,id):
        if request.user.is_autheticated and request.user.is_superuser:
            tema = self.get_object(request,id)
            serializer = ImagemSerializer(instance=tema, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self,request,id):
        if request.user.is_autheticated and request.user.is_superuser:
            tema = self.get_object(request,id)
            tema.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
