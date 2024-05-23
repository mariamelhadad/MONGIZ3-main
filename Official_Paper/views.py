from django.shortcuts import get_object_or_404
from Official_Paper.models import paper
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from Official_Paper.serializer import papersSerializer
from rest_framework.response import Response


class offcial_papers(APIView):
       permission_classes=[IsAuthenticated]
       def get(self,request):
          user=request.user
          Message =get_object_or_404(paper,User=user) 
          serializer = papersSerializer(Message)
          return Response(serializer.data,status=status.HTTP_200_OK)
