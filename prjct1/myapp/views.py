from django.shortcuts import render
from .serailizer import userserailizer
from rest_framework import viewsets
from .models import CustomUser
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


User = get_user_model()
# Create your views here.
class Userviewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=userserailizer
    

class userregister(APIView):
    def post(self,request,format=None):
        try:
            user=request.data.get('user') 
            print('user called',user)  
            user1=User(username=user['username'],password=make_password(user['password']),phone=user['phone'])
            user1.is_active = True
            user1.save()
            print('user1',user1)
            user2={'status':1}
            return JsonResponse(user2,safe=False)
        except Exception as e:
            print(e)
            user2={'status':0}
            return JsonResponse(user2,safe=False)


class profile(APIView):
    def get(self,request):
        user = request.user

        try:
            user_data = {"uaername":user.username,
                     "phone":user.phone}
        except Exception as e:
            print(e)
        return JsonResponse(user_data)
        
