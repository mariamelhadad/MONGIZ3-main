from django.shortcuts import render,get_object_or_404
from .models import Home_page
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import status
from .serialization import homeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import tokens

class Home(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data = get_object_or_404(Home_page,User=user)
        serialize = homeSerializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
    
    
    


