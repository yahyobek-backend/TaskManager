from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('Yangi', 'Yangi'),
            ('Jarayonda', 'Jarayonda'),
            ('Yakunlandi', 'Yakunlandi'),
        ),
        default='Yangi'
    )
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
