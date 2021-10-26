from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators = [RegexValidator(
            regex = r'^@\w{3,}$',
            message = 'Username must consist of @ followed by at least 3 alphanumaricals'
        )]
    )

    first_name = models.CharField(
        max_length = 50,
        unique = False,
        blank = False
    )

    last_name = models.CharField(
        max_length = 50,
        unique = False,
        blank = False
    )

    email = models.EmailField(
        max_length = 254,
        unique = True,
        blank = False
    )

    bio = models.CharField(
        max_length = 520,
        unique = False,
        blank = True
    )



class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(
        max_length = 280,
        unique = False,
        blank = False
    )
    created_at = models.DateTimeField(auto_now_add = True, blank = False)

    class Meta:
        ordering = ["-created_at"]
