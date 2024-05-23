from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serialization import *
from .models import *
# Create your views here.
class personal_id_card(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
            data=request.data
            user=request.user
            if data['National_ID']==user.national_id:
              data['Sender']=user.pk
              serialize=PersonalIDSerialization(data=data)
              if serialize.is_valid():
                 serialize.save()
                 return Response({"msg":"Your request sent","Your request":serialize.data},status=status.HTTP_201_CREATED)
              else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"msg":"National_id doesnt match"})    
               
class personal_driving_license(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
            user=request.user
            data=request.data
            if data['National_ID']==user.national_id:    
              data['Sender']=user.pk
              serialize=PersonalDrivingLicenseSerialization(data=data)
              if serialize.is_valid():
                 serialize.save()
                 return Response({"msg":"Your request sent","Your request":serialize.data},status=status.HTTP_201_CREATED)
              else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"msg":"National_id doesnt match"})   
    
            