from django.db import models

# Create your models here.
class Lead(models.Model):
    post_id = models.CharField(max_length=10, primary_key=True) # Original post id as the primary key of our lead table
    title = models.TextField()
    content = models.TextField()
    posted_at = models.DateTimeField()
    url = models.URLField(max_length=500)





















