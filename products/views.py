from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({'sucess' : "Hurray up dud"})

class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductByCategoryView(APIView):
    def get(self, request):
        category = self.request.query_params.get('category')
#        product = self.request.query_params.get('product')
        if category:
            queryset = Product.objects.filter(category__Category_name = category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'Found':len(serializer.data),
        'data': serializer.data})