from django.contrib.auth.models import User
from rest_framework import serializers

from numbersapi.models import Conversion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "first_name", "last_name", "email"]


class ConversionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversion
        fields = ["url", "input_number", "output_words", "created_by", "created_at"]
