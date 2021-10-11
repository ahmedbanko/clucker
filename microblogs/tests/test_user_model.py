from django.test import TestCase
from microblogs.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

""" Unit test for the user model"""
class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            password = 'Password123',
            bio = 'The quick brown fox jumps over the lazy dog.'
        )
 # ***** TESTS FOR USER *****
    def test_valid_user(self):
        self._assert_user_is_valid()

 # ***** TESTS FOR USERNAME *****
    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_30_character_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_over_30_character_long(self):
         self.user.username = '@' + 'x' * 30
         self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        self.user.username = self.second_user().username
        self._assert_user_is_invalid()

    def test_username_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumaricals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumaricals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_must_contain_only_1_at(self):
        self.user.username = '@@j0hndoe'
        self._assert_user_is_invalid()


 # ***** TESTS FOR FIRST_NAME *****
    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_first_name_can_be_30_character_long(self):
        self.user.first_name = 'x' * 50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_over_50_character_long(self):
         self.user.first_name = 'x' * 51
         self._assert_user_is_invalid()

    def test_first_name_may_not_be_unique(self):
         self.user.first_name = self.second_user().first_name
         self._assert_user_is_valid()


 # ***** TESTS FOR LAST_NAME *****
    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_can_be_30_character_long(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()

    def test_last_name_cannot_be_over_50_character_long(self):
         self.user.last_name = 'x' * 51
         self._assert_user_is_invalid()

    def test_last_name_may_not_be_unique(self):
         self.user.last_name = self.second_user().last_name
         self._assert_user_is_valid()


 # ***** TESTS FOR EMAIL*****
    def test_email_cannot_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        self.user.email = self.second_user().email
        self._assert_user_is_invalid()

    def test_email_must_be_valid(self):
        try:
            validate_email(self.user.email)
        except(ValidationError):
            self.fail('Email should be valid')

    def test_email_format_must_be_valid(self):
        self.user.email = '@mbanko@example.org'
        self._assert_user_is_invalid()


 # ***** TESTS FOR BIO *****
    def test_bio_may_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_bio_can_be_520_character_long(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_bio_cannot_be_over_520_character_long(self):
         self.user.bio = 'x' * 521
         self._assert_user_is_invalid()

    def test_bio_may_not_be_unique(self):
         self.user.bio = self.second_user().bio
         self._assert_user_is_valid()






    def second_user(self):
        user = User.objects.create_user(
            '@janedoe',
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'janedoe@example.org',
            password = 'Password123',
            bio = "Janedoe's Profile"
        )
        return user


    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')


    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
