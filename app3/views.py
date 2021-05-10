from django.shortcuts import render , redirect
from .models import Category
from .serializers import Cat_serializer
from rest_framework import generics
from rest_framework import mixins
#from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


class Cat_create(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = Cat_serializer
    queryset = Category.objects.all()

    def post(self , request,*args,**kwargs):
        return self.create(request , *args,**kwargs) 

class Cat_get(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class = Cat_serializer
    queryset = Category.objects.all()
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  

        
class Cat_put(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    serializer_class = Cat_serializer
    queryset = Category.objects.all()

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    

    

