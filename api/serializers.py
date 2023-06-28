from rest_framework import serializers

from mainapp.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name", "created_at", "updated_at"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "enrollment", "school", "created_at", "updated_at"]


class SchoolWithStudentSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = School
        fields = ["id", "name", "created_at", "updated_at", "students"]
        depth = 1
