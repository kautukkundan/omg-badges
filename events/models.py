from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.core.validators import MinValueValidator
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


class Session(BaseModel):
    sessionId = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name      = models.CharField(max_length=150, null=False, blank=False)
    badge     = models.ForeignKey('badges.Badge', null=True, on_delete=models.SET_NULL)
    start     = models.DateTimeField(null=False)
    end       = models.DateTimeField(null=False)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(end__gt=F('start')), name='check_start_date',
            ),
        ]

    def __str__(self):
        return self.sessionId


class SessionCountSpecial(BaseModel):
    count = models.IntegerField(validators=[MinValueValidator(1)])
    badge = models.ForeignKey('badges.Badge', null=True, on_delete=models.SET_NULL)


class PersonSession(BaseModel):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ManyToManyField('Session')

    def __str__(self):
        return self.email