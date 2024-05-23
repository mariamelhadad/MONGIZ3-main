from django.shortcuts import get_object_or_404
from .models import educational_state
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import educational_state_serializer
from rest_framework.response import Response
# Create your views here.

class Educational_State(APIView):
       permission_classes=[IsAuthenticated]
       def get(self,request):
          user=request.user
          data =get_object_or_404(educational_state,User=user) 
          serializer = educational_state_serializer(data)
          return Response(serializer.data,status=status.HTTP_200_OK)
      

