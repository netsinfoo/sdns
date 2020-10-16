from rest_framework.viewsets import ModelViewSet
from sdns.models import Register
from .serializers import RegisterSerializer

class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer