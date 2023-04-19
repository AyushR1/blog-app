from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=False,editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        abstract = True

class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blogs')
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blogs', null = True, blank = True)