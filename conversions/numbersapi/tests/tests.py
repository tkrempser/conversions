import json

import factory
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django_mock_queries.mocks import MockSet
from numbersapi.models import Conversion
from numbersapi.tests.factories import ConversionFactory, UserFactory
from numbersapi.views import ConversionViewSet, UserViewSet


@pytest.mark.django_db
class TestUserViewSet:
    def test_list(self, mocker, rf):
        url = reverse("user-list")
        request = rf.get(url)
        qs = MockSet(
            UserFactory.build(),
            UserFactory.build(),
            UserFactory.build(),
        )
        view = UserViewSet.as_view({"get": "list"})

        mocker.patch.object(UserViewSet, "get_queryset", return_value=qs)

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_create(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=UserFactory)
        valid_data_dict["url"] = None
        url = reverse("user-list")
        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(User, "save")
        view = UserViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict

    def test_update(self, mocker, rf):
        old_user = UserFactory.build()
        new_user = UserFactory.build()
        user_dict = {
            "url": None,
            "username": new_user.username,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
        }
        url = reverse("user-detail", kwargs={"pk": old_user.id})
        request = rf.put(
            url, content_type="application/json", data=json.dumps(user_dict)
        )
        mocker.patch.object(UserViewSet, "get_object", return_value=old_user)
        mocker.patch.object(User, "save")
        view = UserViewSet.as_view({"put": "update"})

        response = view(request, pk=old_user.id).render()

        assert response.status_code == 200
        assert json.loads(response.content) == user_dict

    def test_delete(self, mocker, rf):
        user = UserFactory.build()
        url = reverse("user-detail", kwargs={"pk": user.id})
        request = rf.delete(url)
        mocker.patch.object(UserViewSet, "get_object", return_value=user)
        del_mock = mocker.patch.object(User, "delete")
        view = UserViewSet.as_view({"delete": "destroy"})

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called


@pytest.mark.django_db
class TestConversionViewSet:
    def test_list(self, mocker, rf):
        url = reverse("conversion-list")
        request = rf.get(url)
        qs = MockSet(
            ConversionFactory.build(),
            ConversionFactory.build(),
            ConversionFactory.build(),
        )
        view = ConversionViewSet.as_view({"get": "list"})

        mocker.patch.object(ConversionViewSet, "get_queryset", return_value=qs)

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_update(self, mocker, rf):
        old_conversion = ConversionFactory.build()
        new_conversion = ConversionFactory.build()
        conversion_dict = {
            "url": None,
            "input_number": new_conversion.input_number,
            "output_words": old_conversion.output_words,
            "created_by": old_conversion.created_by,
            "created_at": old_conversion.created_at,
        }
        url = reverse("conversion-detail", kwargs={"pk": old_conversion.id})
        request = rf.put(
            url, content_type="application/json", data=json.dumps(conversion_dict)
        )
        mocker.patch.object(
            ConversionViewSet, "get_object", return_value=old_conversion
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"put": "update"})

        response = view(request, pk=old_conversion.id).render()

        assert response.status_code == 200
        assert json.loads(response.content) == conversion_dict

    def test_delete(self, mocker, rf):
        Conversion = ConversionFactory.build()
        url = reverse("conversion-detail", kwargs={"pk": Conversion.id})
        request = rf.delete(url)
        mocker.patch.object(ConversionViewSet, "get_object", return_value=Conversion)
        del_mock = mocker.patch.object(Conversion, "delete")
        view = ConversionViewSet.as_view({"delete": "destroy"})

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called

    def test_convert_number_0(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 0
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content)["output_words"] == "zero"

    def test_convert_number_22(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 22
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content)["output_words"] == "twenty-two"

    def test_covert_number_105(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 105
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content)["output_words"] == "one hundred five"

    def test_covert_number_1129(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 1129
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert (
            json.loads(response.content)["output_words"]
            == "one thousand one hundred twenty-nine"
        )

    def test_covert_number_99999(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 99999
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert (
            json.loads(response.content)["output_words"]
            == "ninety-nine thousand nine hundred ninety-nine"
        )

    def test_covert_number_1000000000(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 1000000000
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content)["output_words"] == "one billion"

    def test_covert_number_81020010000099(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 81020010000099
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert (
            json.loads(response.content)["output_words"]
            == "eighty-one trillion twenty billion ten million ninety-nine"
        )

    def test_covert_number_9223372036854775807(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 9223372036854775807
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 201
        assert (
            json.loads(response.content)["output_words"]
            == "nine quintillion two hundred twenty-three quadrillion three hundred "
            "seventy-two trillion thirty-six billion eight hundred fifty-four million "
            "seven hundred seventy-five thousand eight hundred seven"
        )

    def test_covert_number_1000000000000000000000(self, mocker, rf):
        valid_data_dict = factory.build(dict, FACTORY_CLASS=ConversionFactory)
        valid_data_dict["url"] = None
        valid_data_dict["input_number"] = 1000000000000000000000
        url = reverse("conversion-list")

        request = rf.post(
            url, content_type="application/json", data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(Conversion, "save")
        view = ConversionViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 400
        assert json.loads(response.content) == {
            "input_number": [
                "Ensure this value is less than or equal to 9223372036854775807."
            ]
        }
