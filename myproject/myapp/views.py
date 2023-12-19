from django.shortcuts import render
from rest_framework import viewsets
from .models import MyApp
from .serializers import MyAppSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MyAppViewSet(viewsets.ModelViewSet):
    serializer_class = MyAppSerializer
    queryset = MyApp.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

