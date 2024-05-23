from django.shortcuts import get_object_or_404
from .models import social_state,Family
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import social_state_serializer,Family_serializer
from rest_framework.response import Response


class Social(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data = get_object_or_404(social_state,User=user)
        serialize = social_state_serializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
    
class Social_Family(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data = get_object_or_404(Family,User=user)
        serialize = Family_serializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
  

