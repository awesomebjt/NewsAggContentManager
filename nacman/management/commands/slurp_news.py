from django.core.management.base import BaseCommand, CommandError
from nacman.models import *
import feedparser


class Command(BaseCommand):
    help = 'slurps up links to news stories using defined publication feeds'

    def handle(self, *args, **options):
        feeds = PublicationFeed.objects.all()
        for feed in feeds:
            d = feedparser.parse(feed.rss_url)
            print("Parsing "+d.feed.title)
            for entry in d.entries:
                print("{} - {} - {}".format(d.feed.title, entry.published, entry.title))