from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

class BaseModel(models.Model):
    archived   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self):
        self.archived = True
        super().save()

    class Meta:
        abstract = True

class Profile(BaseModel):
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def create_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  

post_save.connect(create_profile, sender=User) 