from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from .serialization import  *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import  APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class report(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        data = request.data
        user=request.user
        data['Sender']=user.pk
        serializer = ReportSerialize(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your issue sent","your issue":serializer.data}, status=status.HTTP_201_CREATED) 
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    