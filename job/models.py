# -*- coding: utf-8 -*-


from django.db import models
Job_Type=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100,null=1)
    job_type = models.CharField(max_length=20,choices=Job_Type)
    description = models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=0)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title