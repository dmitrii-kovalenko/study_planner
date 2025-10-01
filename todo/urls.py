from django.urls import path
from todo import views

app_name = "todo"
urlpatterns = [

    path("", views.Start.as_view(), name="start"),
    path("subject/create/", views.SubjectCreateView.as_view(), name="subject_create"),
    path("subject/list/", views.SubjectListView.as_view(), name="subject_list"),
    path("subject/update/<int:pk>/", views.SubjectUpdateView.as_view(), name="subject_update"),
    path("subject/delete/<int:pk>/", views.SubjectDeleteView.as_view(), name="subject_delete"),
    path("global_overview/", views.GlobalOverview.as_view(), name="global_overview"),
    path("subject/<int:pk>", views.SubjectDetailView.as_view(), name="subject_details"),
    path("assignment/<int:pk>", views.AssignmentCreateView.as_view(), name="assignment_create"),
    path("assignment/update)/<int:pk>/", views.AssignmentCreateView.as_view(), name="assignment_update"),
    path("assignments/<int:pk>/manage/", views.AssignmentsManageView.as_view(), name="assignments_manage"),
]