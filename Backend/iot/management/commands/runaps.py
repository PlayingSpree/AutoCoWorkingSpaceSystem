from django.core.management.base import BaseCommand

from iot.job import setup


class Command(BaseCommand):
    help = "Runs apscheduler."
    scheduler = None

    def handle(self, *args, **options):
        setup()
