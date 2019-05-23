from django.db import models


class Link(models.Model):
    text = models.TextField()
    sended = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Pic(models.Model):
    pic = models.ImageField(upload_to="images/")
    sended = models.BooleanField(default=False)
