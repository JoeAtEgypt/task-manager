from django.contrib.auth import get_user_model as user
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            created_user, created = user().objects.get_or_create(
                email="admin@joeshak.com",
                username="admin",
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
            if created:
                created_user.set_password("12345")
                created_user.save()
            print("current admin : ", created_user)
        except Exception as e:
            raise CommandError(e)
