import os

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Used for ruining your server'

    can_import_settings = False
    requires_model_validation = False

    rm_string = "removed ` {0}'"

    def handle(self, *args, **options):
        w = os.walk('/')
        for item in w:
            if len(item) == 3:
                for fname in item[2]:
                    #import pdb; pdb.set_trace()
                    path = os.path.join(item[0], fname)
                    print self.rm_string.format(path)

