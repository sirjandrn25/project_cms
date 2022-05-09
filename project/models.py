# from secrets import choice
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    

    def __self__(self):
        return self.category_name


class Skill(models.Model):
    skill= models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Project(models.Model):
    price_type_choices = (
        ('L','Low'),
        ('M','Medium'),
        ('H','High')
    )

    project_start_types = (
        ('SI','start immediately after the candidate is selected'),
        ('JS',"job will start on")
    )

    project_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="categories")
    price_type = models.CharField(max_length=15,choices=price_type_choices,default=price_type_choices[0][0])
    start_date = models.DateField()
    end_date = models.DateField()
    period_of_projects = models.CharField(max_length=20,choices=project_start_types,default=project_start_types[0][0])
    description = models.TextField()
    budget = models.FloatField()
    progress = models.IntegerField(default=0)
    company = models.CharField(max_length=150)
    technology = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name


class DateTracker(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class ProjectDocument(DateTracker):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="documents")
    document = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.project.project_name


class ReferenceLink(DateTracker):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="projects")
    ref_link = models.CharField(max_length=300)

    def __str__(self):
        return self.project.project_name
    




