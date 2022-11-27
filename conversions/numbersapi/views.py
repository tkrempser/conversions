from django.contrib.auth.models import User
from django.utils import timezone
from numbersapi.models import Conversion
from numbersapi.serializers import ConversionSerializer, UserSerializer
from numbersapi.utils import convert_number_to_words
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConversionViewSet(viewsets.ModelViewSet):
    queryset = Conversion.objects.all()
    serializer_class = ConversionSerializer

    def perform_create(self, serializer):
        input_number = serializer.validated_data["input_number"]
        output_words = convert_number_to_words(input_number)

        serializer.save(output_words=output_words)
