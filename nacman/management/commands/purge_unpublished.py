from django.core.management.base import BaseCommand, CommandError
from nacman.models import *
import feedparser
import datefinder


class Command(BaseCommand):
    help = 'slurps up links to news stories using defined publication feeds'

    def handle(self):
        Item.objects.filter()
