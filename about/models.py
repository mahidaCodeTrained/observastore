from django.db import models

# Create your models here.


class AboutPage(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    mission = models.TextField()
    history = models.TextField()
    why_shop_here = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
