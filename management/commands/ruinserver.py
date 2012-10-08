import os

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Used for ruining your server'

    def handle(self, *args, **options):
        pass
