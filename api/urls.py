from django.urls import path

from api.views import (
    SchoolDetailAPIView,
    SchoolWithStudentsAPIView,
    StudentDetailAPIView,
)

urlpatterns = [
    path("school/<int:pk>/", SchoolDetailAPIView.as_view(), name="school-detail"),
    path("student/<int:pk>/", StudentDetailAPIView.as_view(), name="student-detail"),
    path(
        "schools-with-students/<int:pk>/",
        SchoolWithStudentsAPIView.as_view(),
        name="school-with-student-detail",
    ),
]
