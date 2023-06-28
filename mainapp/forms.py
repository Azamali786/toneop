from django import forms

from mainapp.models import School, Student


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ("name",)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "enrollment", "school")
