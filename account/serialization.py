from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  *
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import  urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import *
class registerationserialization(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'first_name':{'required':True,},
            'last_name':{'required':True,},
            'password':{'required':True,'min_length':8},
            'email':{'required':True,},
            'national_id':{'required':True,'min_length':13},
            'phone_number':{'required':True,},
            'birth_dt':{'required':True,},
        }
class loginserialize(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['national_id','password',]        

class profileserializer(serializers.ModelSerializer):
    class Meta:
      model=User
      fields='__all__'        

class changepasswordserialize(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)    
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)    
    class Meta:
        model=User
        fields=['password','password2']
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password !=password2:
            raise serializers.ValidationError({"Password doesn't match"})  
        user.set_password(password)
        user.save()
        return  attrs      
class sendpasswordresetemailserialize(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email']
    def validate(self,attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists:
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print('ecoded uid',uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print('password reset token',token)
            link='http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('password reset link',link)
            body='click following link to reset your password'+link
            data={
                'subject':'reset your password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("This Email is not registered")
            
            
            
class userpasswordresetserialize(serializers.ModelSerializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = User.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
       PasswordResetTokenGenerator().check_token(user, token)
       raise serializers.ValidationError('Token is not Valid or Expired')
    
class updateserialize(serializers.ModelSerializer):
    model=User
    fields="__all__"