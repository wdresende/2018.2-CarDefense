from rest_framework import viewsets
from cardefense.models import User
from cardefense.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
