from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE


# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    
 
    def get_name(Category):
        return self.Name

    def get_description(self):
        return self.Description

    def __str__(self):
        return self.Name + '__' + self.Description



class  projects(models.Model):
    project_topic = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    project_title = models.CharField(max_length=250)
    submitted_by = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    project_file = models.FileField(blank=True, null = True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to = 'media', max_length = 100, blank=True, null = True)
     

    

    def __str__(projects):
        return projects.project_title + ' __ ' + projects.submitted_by + ' __ ' + projects.description

    def get_topic(self):
        return self.project_topic

    def get_name(self):
        return self.project_title

    def get_owner(self):
        return self.submitted_by

    def get_description(self):
        return self.description

    


class submit(models.Model):
    file_upload = models.FileField(upload_to="%m/%d/%y")
    