from rest_framework import serializers
from .models import Authorities,Health,Business

class AuthoritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorities
        fields = '__all__'

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'