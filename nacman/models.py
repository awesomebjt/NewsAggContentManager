from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=200)
    base_dir = models.CharField(max_length=500)
    content_dir = models.CharField(max_length=500)
    links_file = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class RSSFeed(models.Model):
    name = models.CharField(max_length=200)
    rss_url = models.CharField(max_length=1000)
    default_site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1000, null=True)
    pub_date = models.DateTimeField('datetime published at origin', null=True)
    author = models.CharField(max_length=200)
    text_body = models.TextField(max_length=10000, null=True)
    origin_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1000, null=True)
    default_site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} - {}".format(self.origin_feed, self.title)


class Post(models.Model):
    post = models.ForeignKey(Item, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    post_date = models.DateTimeField('datetime posted on site', null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.site, self.post)


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    html_body = models.TextField(max_length=10000, null=True)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return "{}x{} - {}".format(self.width, self.height, self.title)


