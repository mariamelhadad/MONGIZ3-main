from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serialization import *
# Create your views here.
class medical_history(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = request.user
        data=get_object_or_404(medicalhistory,User=user)
        serialize=medicalhistoryserialization(data)
        return Response(serialize.data,status=status.HTTP_200_OK)