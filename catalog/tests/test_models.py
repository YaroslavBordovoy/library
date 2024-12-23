from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelsTests(TestCase):
    def test_literary_format_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        self.assertEqual(str(literary_format), literary_format.name)

    def test_author_str(self):
        author = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(author),
            f"{author.username}: ({author.first_name} {author.last_name})"
        )

    def test_book_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(
            title="test",
            price=15.5,
            format=literary_format,
        )
        self.assertEqual(
            str(book),
            f"{book.title} (price: {book.price}, format: {book.format})"
        )

    def test_create_author_with_pseudonym(self):
        author = get_user_model().objects.create_user(
            username="test",
            password="test123",
            pseudonym="test pseudonym"
        )
        self.assertEqual(author.username, "test")
        self.assertEqual(author.pseudonym, "test pseudonym")
        self.assertTrue(author.check_password("test123"))