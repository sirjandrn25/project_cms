from django.contrib import admin
from .models import *
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

admin.site.register(Category)
# admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ProjectDocument)
admin.site.register(ReferenceLink)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name','start_date']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
