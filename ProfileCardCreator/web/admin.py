from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.contrib.auth.models import Group, User
from ProfileCardCreator.web.models import Category, FieldOfWork, Item, Subtask, TodoTask


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)
    ordering = ('Name',)


admin.site.register(Category, CategoryAdmin)


class FieldOfWorkAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Category')
    ordering = ('Name',)


admin.site.register(FieldOfWork, FieldOfWorkAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'TodoTask', 'display_thumbnail')
    ordering = ('Name',)

    def display_thumbnail(self, obj):
        if obj.ImageUrl:
            html = format_html('<img src="{}" width="100" height="100" />', obj.ImageUrl)
            print(html)
            return html
        else:
            return 'No Image'

    display_thumbnail.short_description = 'Thumbnail'


admin.site.register(Item, ItemAdmin)


class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('Title', 'TodoTask')
    search_fields = ('Title',)
    ordering = ('Title',)


admin.site.register(Subtask, SubtaskAdmin)


class TodoTaskAdmin(admin.ModelAdmin):
    list_display = (
        'Title', 'Deadline', 'IsCompleted', 'FieldOfWork', 'Creator', 'Assignee')
    list_filter = ('IsCompleted',)
    search_fields = ('Title',)
    ordering = ('Title',)


admin.site.register(TodoTask, TodoTaskAdmin)


