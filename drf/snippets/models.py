from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

"""Create models for the snippets app."""

#get lexers from pygments if they have aliases
LEXERS = [item for item in get_all_lexers() if item[1]]

#get language choices from lexers
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

#get styles from pygments
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Snippet(models.Model):
    """Snippets model to store code snippets."""
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(default='', max_length=100, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created_at']

