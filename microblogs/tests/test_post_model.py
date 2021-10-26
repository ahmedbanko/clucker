from django.test import TestCase
from microblogs.models import User, Post
from django.core.exceptions import ValidationError
from django.utils.timezone import datetime
from .helpers import LogInTester

""" Unit test for the user model"""
class PostModelTestCase(TestCase, LogInTester):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            password = 'Password123',
            bio = 'The quick brown fox jumps over the lazy dog.'
        )

        self.post = Post.objects.create(
            author = self.user,
            text = 'Post text body',
        )

 # ***** TESTS FOR AUTHOR *****
    def test_valid_author(self):
        self.client.login(username = '@johndoe', password = 'Password123')
        self.assertTrue(self._is_logged_in())


    def test_author_cannot_be_blank(self):
        self.post.author = None
        self._assert_post_is_invalid()

    def test_post_can_be_280_characters(self):
        self.post.text = 'X' * 280
        self._assert_post_is_valid()

    def test_post_cannot_be_over_280_characters(self):
         self.post.text = 'X' * 281
         self._assert_post_is_invalid()

    def test_created_at_cannot_be_blank(self):
        self.post.created_at = ''
        self._assert_post_is_invalid()

    def test_created_at_format_is_valid(self):
        self.assertTrue(isinstance(self.post.created_at, datetime))


    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except(ValidationError):
            self.fail('Test post should be valid')
