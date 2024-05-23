from django.shortcuts import get_object_or_404
from .models import message
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serialization import msg_serializer
from rest_framework.response import Response


class Message(APIView):
       permission_classes=[IsAuthenticated]
       def get(self,request):
          user=request.user
          Message =get_object_or_404(message,User=user) 
          serializer = msg_serializer(Message)
          return Response(serializer.data,status=status.HTTP_200_OK)
