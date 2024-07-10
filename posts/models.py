from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag


class Post(models.Model):
    """
    Post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_vpipga', blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
