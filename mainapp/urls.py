from django.urls import path

from mainapp import views

app_name = "mainapp"


urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("get-schools-list/", views.SchoolListView.as_view(), name="school_list"),
    path("create-school/", views.SchoolCreateView.as_view(), name="create_school"),
    path(
        "update-school/<int:pk>/",
        views.SchoolUpdateView.as_view(),
        name="update_school",
    ),
    path(
        "delete-school/<int:pk>/",
        views.SchoolDeleteView.as_view(),
        name="delete_school",
    ),
    path("get-students-list/", views.StudentListView.as_view(), name="student_list"),
    path("create-student/", views.StudentCreateView.as_view(), name="create_student"),
    path(
        "update-student/<int:pk>/",
        views.StudentUpdateView.as_view(),
        name="update_student",
    ),
    path(
        "delete-student/<int:pk>/",
        views.StudentDeleteView.as_view(),
        name="delete_student",
    ),
]
