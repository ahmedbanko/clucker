from django.test import TestCase
from microblogs.models import User, Post
from django.core.exceptions import ValidationError
from django.utils.timezone import datetime

""" Unit test for the user model"""
class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            password = 'Password123',
            bio = 'The quick brown fox jumps over the lazy dog.'
        )

        self.post = Post.objects.create_post(
            self.user,
            text = 'Post text body'
        )

 # ***** TESTS FOR AUTHOR *****
    def test_valid_author(self):
        self._assert_user_is_valid()


    # def test_author_cannot_be_blank(self):
    #     pass
    #
    # def test_post_can_be_280_characters(self):
    #     pass
    #
    # def test_post_cannot_be_over_280_characters(self):
    #      pass
    #
    # def test_created_at_cannot_be_blank(self):
    #     pass
    #
    # def test_created_at_format_is_valid(self):
    #     pass


    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_post_is_invalid(self):
        pass

    def _assert_post_is_valid(self):
        pass
