from django.db import models
from django.core.exceptions import ValidationError
import re

# found at:
# https://stackoverflow.com/questions/16982625
# /only-accept-alphanumeric-characters-and-underscores-for-a-string-in-python
def validate_tag_name(value):
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValidationError(
            'Tag name can only be alphanumeric characters and underscores.')


class Tag(models.Model):
    """
    Tag model for hashtags.
    """
    name = models.CharField(
        max_length=100, 
        unique=True, 
        validators=[validate_tag_name],
        null=False
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
