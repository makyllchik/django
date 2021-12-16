from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    comments = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="", null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"
