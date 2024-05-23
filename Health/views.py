from django.shortcuts import render,get_object_or_404
from .models import health_state
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import healthstate_serializer
from rest_framework.response import Response



class Health_State(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data = get_object_or_404(health_state,User=user)
        serialize = healthstate_serializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
    

