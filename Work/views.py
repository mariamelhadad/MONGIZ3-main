from django.shortcuts import render
from .models import work_career
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Work.serializer import WorkSerializer
from rest_framework.response import Response

class work(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serializer=WorkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data sent","data":serializer.data},status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
             
        
