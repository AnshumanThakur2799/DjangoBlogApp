from django.shortcuts import render
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib.auth.models import User
# Create your views here.

class RegisterUser(APIView):

    def post(self , request):
        try:
            serializer = UserSerializers(data=request.data)

            if not serializer.is_valid():
                return JsonResponse({
                    "status": status.HTTP_403_FORBIDDEN,
                    "error" : serializer.errors,
                    "message" : "some error occured while registring"
                }) 

            serializer.save()
            user = User.objects.get(username=serializer.data.get('username'))
            token_obj, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({
                "status": status.HTTP_200_OK,
                "payload": serializer.data,
                "token": str(token_obj),
                "message" : "user registered successfully"
            })
    
        except Exception as e:
            raise HttpResponseBadRequest(str(e))

        