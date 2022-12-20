import factory
from django.contrib.auth.models import User
from numbersapi.models import Conversion


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.faker.Faker("word")
    first_name = factory.faker.Faker("first_name")
    last_name = factory.faker.Faker("last_name")
    email = factory.faker.Faker("ascii_email")


class ConversionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Conversion
        exclude = ['created_by']

    input_number = factory.Iterator(
        [
            "0",
            "1",
            "12",
            "33",
            "100",
            "1155",
            "1000000",
        ]
    )
    created_at = factory.faker.Faker("date")
