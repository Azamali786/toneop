from django.contrib import admin

from mainapp.models import School, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("id", "name")
    list_per_page = 25
    list_filter = ("created_at", "updated_at")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "enrollment", "school")
    list_display_links = ("id", "name")
    list_per_page = 25
    list_filter = ("created_at", "updated_at")


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
