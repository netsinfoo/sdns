from rest_framework.serializers import ModelSerializer
from sdns.models import Register

class RegisterSerializer(ModelSerializer):
    
    class Meta:
        model = Register
        fields = ('ip', 'host', 'domain')