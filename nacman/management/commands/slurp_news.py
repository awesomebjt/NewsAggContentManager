from django.core.management.base import BaseCommand, CommandError
from nacman.models import *
import feedparser
import datefinder


class Command(BaseCommand):
    help = 'slurps up links to news stories using defined publication feeds'

    def handle(self, *args, **options):
        feeds = RSSFeed.objects.all()
        for feed in feeds:
            d = feedparser.parse(feed.rss_url)
            print("Parsing "+d.feed.title)
            for entry in d.entries:
                if Item.objects.filter(link=entry.link).count() < 1:
                    print("Generating Post: {} - {} - {}".format(
                        d.feed.title,
                        entry.published,
                        entry.title
                    ))
                    i = Item(
                        title=entry.title or '',
                        link=entry.link or '',
                        pub_date=list(datefinder.find_dates(entry.published))[0],
                        text_body=entry.description or '',
                        origin_feed=feed
                    )
                    i.save()