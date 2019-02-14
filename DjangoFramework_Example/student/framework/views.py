from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializerform import ProductSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def productlist(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True).data
        return Response(serializer)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ProductSerializer().data, status=status.HTTP_200_OK)
    return Response({'status': 'Error', 'Message': "only get and post method allowed"},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_details(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(obj)
    return Response(serializer.data)
