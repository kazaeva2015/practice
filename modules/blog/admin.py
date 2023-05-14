from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin


@admin.register(Subject)
class SubjectAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'subject_name', 'slug')
    list_display_links = ('subject_name', 'slug')
    prepopulated_fields = {'slug': ('subject_name',)}

    fieldsets = (
        ('Основная информация', {'fields': ('subject_name', 'slug', 'parent')}),
        ('Описание', {'fields': ('descript',)})
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(City)
admin.site.register(Region)
"""admin.site.register(Post)"""

