from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    archived   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self):
        self.archived = True
        super().save()

    class Meta:
        abstract = True


class Badge(BaseModel):
    badgeId = models.CharField(max_length=20, null=False, blank=False, primary_key=True)
    name    = models.CharField(max_length=150, null=False, blank=False)
    image   = models.ImageField(upload_to='badge/', null=True)

    def __str__(self):
        return self.badgeId


class PersonBadge(BaseModel):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    badge = models.ManyToManyField('Badge', related_name="person_badge")

    def __str__(self):
        return self.user.username

        