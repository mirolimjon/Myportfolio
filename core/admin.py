from django.contrib import admin
from .models import Project, ProjectImages, Contact, Skills
# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']

admin.site.register(Skills, SkillAdmin)


# ProjectImages
class ProjectImagesAdmin(admin.TabularInline):
    model = ProjectImages

# Project 
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesAdmin]
    list_display = ['title', 'project_image_view', 'created']
admin.site.register(Project, ProjectAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
admin.site.register(Contact, ContactAdmin)