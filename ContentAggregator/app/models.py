from django.db import models

# Create your models here.
class PyContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.headline


class ProgContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.headline


class CovidContent(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    pubDate = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.headline


class CovidGoogleNewsContent(models.Model):
    headline = models.CharField(max_length=300)
    url = models.TextField()
    pubDate = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.headline


class CovidMalaysiakiniContent(models.Model):
    headline = models.CharField(max_length=300)
    url = models.TextField()
    pubDate = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.headline
