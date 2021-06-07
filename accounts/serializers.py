from .models import Account
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"

