from django.db import models


class PublicationFeed(models.Model):
    name = models.CharField(max_length=200)
    rss_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datetime published at origin')
    post_date = models.DateTimeField('datetime posted on site')
    author = models.CharField(max_length=200)
    text_body = models.TextField(max_length=10000, null=True)
    origin_feed = models.ForeignKey(PublicationFeed, on_delete=models.CASCADE)
    published = models.BooleanField()
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ', by ' + self.author


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    html_body = models.TextField(max_length=10000, null=True)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return "{}x{} - {}".format(self.width, self.height, self.title)


