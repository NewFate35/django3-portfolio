from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'url']
    # list_filter = ['url']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="250" height="150"')

    get_image.short_description = "Изображение"

admin.site.register(Project, ProjectAdmin)
