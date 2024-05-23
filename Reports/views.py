from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Reports.serialization import ReportSerializer
from rest_framework.response import Response
from .models import *

class Report(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
          user=request.user
          data=request.data
          data['Sender']=user.pk
          serialize = ReportSerializer(data=data)
          if serialize.is_valid():
            serialize.save()
            return Response({"msg":"Your report sent","Your report":serialize.data},status=status.HTTP_200_OK)
          else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
       
      
    
