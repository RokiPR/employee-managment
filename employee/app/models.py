from django.db import models

# Create your models here.

class Employees(models.Model):
    STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    GENDER = (
        ("M", "M"),
        ("F", "F"),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    position = models.CharField(max_length=40, default="")
    status = models.CharField(max_length=10, null=True, choices=STATUS)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    note = models.TextField(blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name