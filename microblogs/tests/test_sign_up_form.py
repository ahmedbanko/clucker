from django.test import TestCase
from django import forms
from microblogs.models import User
from microblogs.forms import SignUpForm


""" Unit test for the sign up form"""
class SignUpTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': '@janedoe',
            'email': 'janedoe@example.org',
            'bio': 'Jane bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }


    # Test if the form accepts valid input data
    def test_valid_sign_up_form(self):
        form = SignUpForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    # Test if the form declines invalid input data
    def test_invalid_sign_up_form(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


     # Test if the form has necessary fields
    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        password_confirmation_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))


     # Test if the new password has an uppercase letter
    def test_password_has_uppercase(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


     # Test if the new password has a lowercase letter
    def test_password_has_lowercase(self):
        self.form_input['new_password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


     # Test if the new password has a number
    def test_password_has_a_number(self):
        self.form_input['new_password'] = 'PasswordABC'
        self.form_input['password_confirmation'] = 'PasswordABC'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


     # Test if the new password matches password confirmation
    def test_password_match_confirmation(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())
