from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Blog(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blogsimg', default='blogsimg/default.png')

    def __str__(self):
        return self.title