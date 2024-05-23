from django.shortcuts import render
from rest_framework.views import  APIView
from  rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serialization import *
# Create your views here.
class Personal_Info(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serialize=PersonalInfoserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data sent","Your data":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class Expereince(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serialize=Expereinceserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data sent","Your data":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class Technical_Skills(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serialize=Technicalskillsserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data sent","Your data":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
class Education(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serialize=Educationserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data sent","Your data":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
      
        
        
class Contact_Info(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serialize=Contact_Infoserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data sent","Your data":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)