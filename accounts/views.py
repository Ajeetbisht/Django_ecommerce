from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username + password)
        #adding user to main
        user = User(username=username, password=password)
        user.set_password(password)
        user.save()
        #token
        refresh = RefreshToken.for_user(user)
        return Response({'status':'Registration done!!!!'
        +'USERNAME :'+username+' PASSWORD :'+password,
        'refresh': str(refresh), 
        'access': str(refresh.access_token)})