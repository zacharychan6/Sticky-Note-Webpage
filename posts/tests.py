from django.test import TestCase
from django.urls import reverse
from .models import sticky_note, Author
# Create your tests here.


class StickyNoteTests(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Test Author")
        sticky_note.objects.create(
            title="Test Sticky Note", content="Test Content", author=author)

    def sticky_has_title(self):
        post = sticky_note.objects.get(id=1)
        self.assertEqual(post.title, "Test Sticky Note")

    def test_content(self):
        post = sticky_note.objects.get(id=1)
        self.assertEqual(post.content, "Test Content")


class StickyNoteViewTests(TestCase):

    def setUp(self):

        author = Author.objects.create(name="Test Author")
        sticky_note.objects.create(
            title="Test Sticky Note", content="Test Content", author=author)

    def test_sticky_list_view(self):

        response = self.client.get(reverse('sticky_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Sticky Note")

    def test_sticky_details_view(self):

        post = sticky_note.objects.get(id=1)
        response = self.client.get(reverse('sticky_details', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Sticky Note")
        self.assertContains(response, "Test Content")
