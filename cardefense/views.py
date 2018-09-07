from django.shortcuts import render
from rest_framework import viewsets
from cardefense.models import Alert
from cardefense.serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
