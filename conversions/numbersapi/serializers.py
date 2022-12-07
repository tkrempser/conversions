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
        read_only_fields = [
            "output_words",
        ]

    def to_representation(self, instance):
        new_representation = super().to_representation(instance)
        new_representation["input_number"] = str(new_representation["input_number"])
        return new_representation
