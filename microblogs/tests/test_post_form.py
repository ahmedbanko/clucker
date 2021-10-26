from django.test import TestCase
from django import forms
from microblogs.models import User, Post
from microblogs.forms import PostForm


""" Unit test for the sign up form"""
class PostFormTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            password = 'Password123',
            bio = 'The quick brown fox jumps over the lazy dog.',
            is_active = True,
        )
        self.form_input = {
            'text': 'some text'
        }


    # Test if the form accepts valid input data
    def test_valid_post_form(self):
        form = PostForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    # Test if the form declines invalid input data
    def test_invalid_post_form(self):
        self.form_input['text'] = ''
        form = PostForm(data = self.form_input)
        self.assertFalse(form.is_valid())


     # Test if the form has necessary fields
    def test_form_has_necessary_fields(self):
        form = PostForm()
        self.assertIn('text', form.fields)
