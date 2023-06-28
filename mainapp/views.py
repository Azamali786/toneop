from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

from mainapp.forms import SchoolForm, StudentForm
from mainapp.models import School, Student


class HomeView(TemplateView):
    template_name = "mainapp/home.html"


class SchoolListView(ListView):
    template_name = "mainapp/school_list.html"
    context_object_name = "schools"

    def get_queryset(self):
        queryset = School.objects.all()
        return queryset


class SchoolCreateView(CreateView):
    model = School
    form_class = SchoolForm
    template_name = "mainapp/create_school.html"
    success_url = reverse_lazy("mainapp:school_list")


class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = "mainapp/school.html"
    context_object_name = "school"


class SchoolDeleteView(DeleteView):
    model = School
    template_name = "mainapp/delete_school.html"
    success_url = reverse_lazy("mainapp:school_list")


class StudentListView(ListView):
    template_name = "mainapp/student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "mainapp/create_student.html"
    success_url = reverse_lazy("mainapp:student_list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "mainapp/student.html"
    context_object_name = "student"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "mainapp/delete_student.html"
    success_url = reverse_lazy("mainapp:student_list")
