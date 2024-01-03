from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import *
from haberler.api.serializers import *

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class GazeteciListCreateAPIView(APIView):

    def get(self,request):
        gazeteciler = Gazeteci.objects.all()
        serializer = GazeteciSerializer(gazeteciler, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = GazeteciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

    def get_object(self,pk):
        haber = get_object_or_404(Haber,pk=pk)
        return haber
    
    def get(self,request,pk):
        haber = self.get_object(pk)
        serializer = HaberSerializer(haber)
        return Response(serializer.data)

    def put(self,request,pk):
        haber = self.get_object(pk)
        serializer = HaberSerializer(haber,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        haber = self.get_object(pk)
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

