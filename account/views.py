from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serialization import *
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens  import RefreshToken
# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class registerationview(APIView):
    def post(self, request,format=None):
        data=request.data
        serialize = registerationserialization(data=data)
        if serialize.is_valid():
            if not User.objects.filter(national_id=request.data['national_id']).exists():
                hashed_password = make_password(request.data['password'])
                serialize.validated_data['password'] = hashed_password
                user=serialize.save()
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg': 'Account created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': 'Account already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialize.errors, status=status.HTTP_403_FORBIDDEN)


class login(APIView):
    def  post(self,request):
        serialize=loginserialize(data=request.data)
        if serialize.is_valid():
            national_id=serialize.validated_data.get('national_id')
            hash_password=make_password(request.data['password'])
            hash_password=serialize.validated_data.get("password")
            user=authenticate(username=national_id,password=hash_password)
            if user:
                token=get_tokens_for_user(user)
                return Response({'token':token,"msg":"login success"},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"user not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serialize.errors)    
       

class userprofile(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serialize=profileserializer(request.user,many=False)
        return Response(serialize.data,status=status.HTTP_200_OK)
                
 
class changepassword(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serialize=changepasswordserialize(data=request.data,context={'user': request.user})
        if serialize.is_valid():
            return Response({"msg":"password changed"},status=status.HTTP_200_OK)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class forget_password(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serialize=sendpasswordresetemailserialize(data=request.data)
        if serialize.is_valid(raise_exception=True):
            return Response({"msg":"password reset link sent.please check your email"},status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST) 
        
          
class userpasswordreset(APIView):
    def post(self,request,uid,token):
        serialize=userpasswordresetserialize(data=request.data,context= {'uid': uid,'token': token})
        if serialize.is_valid(raise_exception=True):
            return Response({"msg":"password reset successfully"},status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST) 
                  
        
   
class Update_User(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request):
        data=request.data  
        user=request.user
        user.first_name=data['first_name']
        user.last_name=data['last_name'] 
        user.birth_dt=data['birth_dt']
        user.email=data['email']
        user.national_id=data['national_id']
        user.phone_number=data['phone_number']
        if user.password!=" ":
            user.password=make_password(data['password'])
        else:
            return Response({"msg":"password cant be none"},status=status.HTTP_403_FORBIDDEN)
        serialize=updateserialize(user)
       
        serialize.save
        return Response({"msg":"updated successfully"},status=status.HTTP_202_ACCEPTED)

        
                
             
             
                         