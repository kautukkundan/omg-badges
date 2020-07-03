from django.db import models
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


class Badge(BaseModel):
    badgeId = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name    = models.CharField(max_length=150, null=False, blank=False)
    image   = models.ImageField(upload_to='badge/', null=True)

    def __str__(self):
        return self.badgeId


class Session(BaseModel):
    sessionId = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name      = models.CharField(max_length=150, null=False, blank=False)
    badge     = models.ForeignKey(Badge, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sessionId


class PersonBadge(BaseModel):
    email = models.CharField(max_length=150, null=False, blank=False, primary_key=True)
    badge = models.ManyToManyField('Badge')

    def __str__(self):
        return self.email


class PersonSession(BaseModel):
    email   = models.CharField(max_length=150, null=False, blank=False, primary_key=True)
    session = models.ManyToManyField('Session')

    def __str__(self):
        return self.email


class EmailUID(BaseModel):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=150, null=False, blank=False)