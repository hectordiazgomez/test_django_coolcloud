# blog/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from myapp.models import Category, Post
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = [
            'Technology', 'Science', 'Health', 'Travel', 'Food'
        ]
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)

        # Create posts
        for i in range(20):  # Create 20 sample posts
            title = f'Sample Post {i+1}'
            content = f'This is the content of sample post {i+1}. It contains some text for testing purposes.'
            excerpt = f'This is the excerpt for sample post {i+1}.'
            created_at = timezone.now() - timezone.timedelta(days=random.randint(0, 365))
            category = Category.objects.order_by('?').first()  # Random category

            Post.objects.create(
                title=title,
                content=content,
                excerpt=excerpt,
                created_at=created_at,
                category=category
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))