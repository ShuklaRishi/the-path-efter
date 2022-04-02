from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    dob = models.DateField(blank=True, null=True)
    QUALIFICATIONS = [
        ("NONE", "NONE"),
        ("PhD", "PhD"),
        ("B.Tech", "B.Tech"),
        ("M.Tech", "M.Tech"),
        ("MBA", "MBA"),
        ("B.Com", "B.Com"),
        ("M.Com", "M.Com"),
        ("BBA", "BBA"),
        ("MBBS", "MBBS"),
        ("MS", "MS"),
        ("MD", "MD"),
        ("LLB", "LLB"),
    ]
    qualification = models.CharField(
        choices=QUALIFICATIONS, default="NONE", blank=True, null=True, max_length=30
    )

    FIELDS = [
        ("Science", "Science"),
        ("Commerce", "Commerce"),
        ("Arts", "Arts"),
        ("Humanity", "Humanity"),
    ]

    fields = models.CharField(
        choices=FIELDS, default="Science", blank=True, null=True, max_length=30
    )
    isStudent = models.BooleanField(default=True)



class Meets(models.Model):
    student = models.ForeignKey(to=MyUser, on_delete=models.CASCADE)
    meet = models.DateField(blank=True, null=True)