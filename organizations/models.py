from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    organization_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.organization_name

class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    # members = models.ManyToManyField(User)
    organization_FK = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name