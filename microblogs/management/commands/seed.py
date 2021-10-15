from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for _ in range(100):
            self.first_name = self.faker.unique.first_name()
            self.last_name = self.faker.unique.last_name()
            User.objects.create_user('@' + self.first_name + self.last_name,
                                    first_name = self.first_name,
                                    last_name = self.last_name,
                                    email = self.faker.unique.email(),
                                    password = self.faker.password(),
                                    bio = f"Hey there!\n My name is {self.first_name}.")
