from django.contrib import admin

from .models import GroupProfile, SiteAppearance


@admin.register(GroupProfile)
class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ("group_name", "class_name", "course_name", "updated_at")


@admin.register(SiteAppearance)
class SiteAppearanceAdmin(admin.ModelAdmin):
    list_display = ("name", "primary_color", "font_family", "updated_by", "updated_at")
