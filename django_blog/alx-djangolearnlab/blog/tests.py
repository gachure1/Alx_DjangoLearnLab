from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post content.')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertIsNotNone(self.post.published_date)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')  # Assuming you have a __str__ method in your Post model