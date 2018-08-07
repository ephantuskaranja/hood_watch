from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hood(models.Model):
    LOCATION_CHOICES=(
        ('MAYOR-ROAD', 'Mayor-Road'),
        ('RONGAI', 'rongai'),
        ('GATAKA', 'gataka'),
        ('OLOLUA', 'ololua')
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=60,choices=LOCATION_CHOICES)
    occupants_count = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length=30, blank=True, null=True)


class Recommendation(models.Model):
    INS_CHOICES =(
        ('PUBLIC', 'public'),
        ('PRIVATE', 'private')
        )
    OUTSTANDING_CHOICES = (
        ('COMMUNISM', 'Communism'),
        ('EXCELLENCE', 'Excellence'),
        ('COMPASION', 'Compasion'),
        ('INTEGRITY', 'Integrity')
        )
       
    institution_name = models.CharField(max_length=50, blank=True, null=True)
    dept = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Hood,on_delete=models.CASCADE,null=True)
    institution_category = models.CharField(max_length=60,choices=INS_CHOICES)
    outstanding = models.CharField(max_length=60,choices=OUTSTANDING_CHOICES)


class Reports(models.Model):
    OUTSTANDING_CHOICES = (
        ('RACISM', 'racism'),
        ('BAD-SERVICES', 'Bad-Services'),
        ('BRIBERY', 'Bribery')
    )
    institution_name = models.CharField(max_length=50, blank=True, null=True)
    dept=models.CharField(max_length=50, blank=True, null=True)
    location=models.ForeignKey(Hood,on_delete=models.CASCADE,null=True)
    institution_category=models.CharField(max_length=60, choices=OUTSTANDING_CHOICES)
