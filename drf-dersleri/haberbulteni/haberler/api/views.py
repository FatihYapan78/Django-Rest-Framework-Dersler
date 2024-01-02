from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import *
from haberler.api.serializers import *

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class HaberListCreateAPIView(APIView):

    def get(self,request):
        haberler = Haber.objects.filter(aktif=True)
        serializer = HaberSerializer(haberler, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = HaberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HaberDetailAPIView(APIView):

    def get_object(self,id):
        haber = get_object_or_404(Haber,id=id)
        return haber
    
    def get(self,request,id):
        haber = self.get_object(id)
        serializer = HaberSerializer(haber)
        return Response(serializer.data)

    def put(self,request,id):
        haber = self.get_object(id)
        serializer = HaberSerializer(haber,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        haber = self.get_object(id)
        haber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








# @api_view(["GET","POST"])
# def haber_list_create_api_view(request):

#     if request.method == "GET":
#         haberler = Haber.objects.filter(aktif=True)
#         serializer = HaberSerializer(haberler, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = HaberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(["GET","PUT","DELETE"])   
# def haber_detail_api_view(request,id):
#     try:
#         haber = Haber.objects.get(id=id)
#     except Haber.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = HaberSerializer(haber)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = HaberSerializer(haber,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         haber.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

