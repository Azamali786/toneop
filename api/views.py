from rest_framework import generics

from api.serializers import (
    SchoolSerializer,
    SchoolWithStudentSerializer,
    StudentSerializer,
)
from mainapp.models import School, Student


class SchoolDetailAPIView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolWithStudentsAPIView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolWithStudentSerializer
