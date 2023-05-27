from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin', 
                password='Pass@123', 
                phone_number='+380981111111',
                city='Lviv'
            )
