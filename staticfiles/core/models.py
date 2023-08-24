from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

# Create your models here.

class Skills(models.Model):
    sid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="tid_",
        alphabet="abcdefg1234",
        unique=True,
    )
    title = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    image = models.ImageField(upload_to='project-image/')
    github = models.URLField(blank=True, null=True)
    g_drive = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def project_image_view(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField('project-files/')
    
    def __str__(self):
        return self.project


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.name    