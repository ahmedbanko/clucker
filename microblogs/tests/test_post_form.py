from django.test import TestCase
from django import forms
from microblogs.models import User, Post
from microblogs.forms import PostForm
from django.urls import reverse

""" Unit test for the post form"""
class PostFormTestCase(TestCase):

    def setUp(self):
        self.url = reverse('feed')
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


    # def test_unsuccesful_post(self):
    #     self.form_input['test'] = ''
    #     before_count = Post.objects.count()
    #     response = self.client.post(self.url, self.form_input)
    #     after_count = Post.objects.count()
    #     self.assertEqual(after_count, before_count)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'feed.html')
    #     form = response.context['form']
    #     self.assertTrue(isinstance(form, PostForm))
    #     self.assertTrue(form.is_bound)
    #

    # def test_succesful_post(self):
    #     before_count = Post.objects.count()
    #     response = self.client.post(self.url, self.form_input, follow = True)
    #     # response_url = reverse('feed')
    #     # self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
    #     # self.assertTemplateUsed(response, 'feed.html')
    #     after_count = Post.objects.count()
    #     self.assertEqual(after_count, before_count+1)
