from django.core.management.base import BaseCommand
from users.models import User
from lesson.models import Lesson,Course

class Command(BaseCommand):
    help = 'Add test students to the database'