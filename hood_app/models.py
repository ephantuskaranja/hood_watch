from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Hood(models.Model):
    MAYOR_ROAD = 'MAYOR_ROAD'
    RONGAI='RONGAI'
    GATAKA='GATAKA'
    OLOLUA='OLOLUA'

    LOCATION_CHOICES=(
        ('MAYOR_ROAD', 'Mayor_Road'),
        ('RONGAI', 'rongai'),
        ('GATAKA', 'gataka'),
        ('OLOLUA', 'ololua')
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=60,choices=LOCATION_CHOICES)
    occupants_count = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.location


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
    desc = models.TextField(max_length=250, blank=True)
    created_at = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.institution_name

    class Meta:
        verbose_name_plural = 'Recommendations'


class Reports(models.Model):
    OUTSTANDING_CHOICES = (
        ('RACISM', 'racism'),
        ('BAD-SERVICES', 'Bad-Services'),
        ('BRIBERY', 'Bribery')
    )

    CATEGORIES =(
        ('PUBLIC', 'public'),
        ('PRIVATE', 'private')
        )
    institution_name = models.CharField(max_length=50, blank=True, null=True)
    dept = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Hood,on_delete=models.CASCADE,null=True)
    outstanding = models.CharField(max_length=60, choices=OUTSTANDING_CHOICES, null=True)
    institution_category = models.CharField(max_length=60, choices=CATEGORIES, blank=True)
    desc = models.TextField(max_length=250, blank= True)
    created_at = models.DateField(default=datetime.now, blank=True)


    def __str__(self):
        return self.outstanding

    class Meta:
        verbose_name_plural ='Reports'

    def save_report(self):
        self.save()