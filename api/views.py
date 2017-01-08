from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from api.serializers import UserSerializer, GroupSerializer
import http

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ReadingViewSet(viewsets.ViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def retrieve(self, request, pk=None):
        conn = http.client.HTTPConnection("10.0.0.11", 5000)
        conn.request("GET", "/api/v1.0/sensor")
        data = conn.getresponse()

        return Response(data)
