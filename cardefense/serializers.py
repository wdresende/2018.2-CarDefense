from rest_framework import serializers
from cardefense.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__' #quais campos da modelo serão utilizados [name]
