from django.contrib import admin

from mainapp.models import School, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "enrollment", "school")


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
