""" Tests of the log in view."""
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import LogInForm

class LogInViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('log_in')


    def test_log_in_url(self):
        self.assertEqual(self.url, '/log_in/')

    def test_get_log_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)


    # def test_unsuccesful_log_in(self):
    #     self.form_input['username'] = 'BAD_USERNAME'
    #     before_count = User.objects.count()
    #     response = self.client.post(self.url, self.form_input)
    #     after_count = User.objects.count()
    #     self.assertEqual(after_count, before_count)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'sign_up.html')
    #     form = response.context['form']
    #     self.assertTrue(isinstance(form, SignUpForm))
    #     self.assertTrue(form.is_bound)
    #
    #
    # def test_succesful_sign_up(self):
    #     before_count = User.objects.count()
    #     response = self.client.post(self.url, self.form_input, follow = True)
    #     after_count = User.objects.count()
    #     self.assertEqual(after_count, before_count+1)
    #     response_url = reverse('feed')
    #     self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
    #     self.assertTemplateUsed(response, 'feed.html')
    #     user = User.objects.get(username = '@janedoe')
    #     self.assertEqual(user.first_name, 'Jane')
    #     self.assertEqual(user.last_name, 'Doe')
    #     self.assertEqual(user.email, 'janedoe@example.org')
    #     self.assertEqual(user.bio, 'Jane bio')
    #     is_password_correct = check_password('Password123', user.password)
    #     self.assertTrue(is_password_correct)
