from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import LiteraryFormat

LITERARY_FORMAT_URL = reverse("catalog:literary-format-list")


class PublicLiteraryFormatTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(LITERARY_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateLiteraryFormatTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_literary_formats(self):
        LiteraryFormat.objects.create(name="drama")
        LiteraryFormat.objects.create(name="poetry")
        response = self.client.get(LITERARY_FORMAT_URL)

        self.assertEqual(response.status_code, 200)

        literary_formats = LiteraryFormat.objects.all()
        self.assertEqual(list(response.context["literary_format_list"]), list(literary_formats))
        self.assertTemplateUsed(response, "catalog/literary_format_list.html")
        