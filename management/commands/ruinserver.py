import os
import signal
import sys

from django.core.management.base import BaseCommand, CommandError

WARNING_STRING = "WARNING: This will ruin your server. Do you wish to continue? [Y/N]\n"
AREYOUSURE = "Are you sure? [Y/N]\n"

times_interrupted = 0

def signal_handler(signal, frame):
    if times_interrupted == 2:
        print 'lol'
        sys.exit(0)
    else:
        times_interrupted += 1

signal.signal(signal.SIGINT, signal_handler)


class Command(BaseCommand):
    help = 'Used for ruining your server'

    can_import_settings = False
    requires_model_validation = False

    rm_string = "removed ` {0}'"
    rmdir_string = "removed directory ` {0}'"

    def handle(self, *args, **options):
        sure = raw_input(WARNING_STRING)
        while True:
            if sure.lower() == 'n': break
            sure  = raw_input(AREYOUSURE)

        w = os.walk('/')
        for item in w:
            if len(item) == 3:
                for fname in item[2]:
                    path = os.path.join(item[0], fname)

            else:
                #import pdb; pdb.set_trace()
                path = os.path.join(item[0])

            print self.rm_string.format(path)
