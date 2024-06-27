from django.db import models

class Tag(models.Model):
    """
    Tag model for hashtags.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
