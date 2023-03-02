from django.shortcuts import render
from .serializer import ProductSerializer
from .serializer import BasketSerializer
from rest_framework.views import APIView
from .models import Product
from .models import Basket
from rest_framework.response import Response
# Create your views here.


class ProductAPIView(APIView):

    def get(self, req):
        products_list = Product.objects.all()
        return Response({'products':ProductSerializer(products_list, many=True).data})

    def post(self, req):
        serializer = ProductSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self,req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error': 'Objectdoes not exists'})

        serializer = ProductSerializer(data=req.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self,req,*args, **kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error': 'Method DELETE not alowed'})

        products_list = Product.objects.get(pk=pk)
        products_list.delete()

        return Response({'post':'delete post ' + str(pk)})
    

class BasketAPIView(APIView):

    def get(self, req):
        basket_list = Basket.objects.all()
        return Response({'basket':ProductSerializer(basket_list, many=True).data})
    
    def post(self, req):
        serializer = BasketSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self,req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Basket.objects.get(pk=pk)
        except:
            return Response({'error': 'Objectdoes not exists'})

        serializer = BasketSerializer(data=req.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def delete(self,req,*args, **kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error': 'Method DELETE not alowed'})
        
        basket_list = Basket.objects.get(pk=pk)
        basket_list.delete()

        return Response({'post':'delete post ' + str(pk)})
    

