from django.db import models


class Check(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

