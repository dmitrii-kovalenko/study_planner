from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from todo.forms import SubjectForm
from todo.models import Subject


class Start(generic.TemplateView):
    template_name = "start.html"

class SubjectCreateView(generic.CreateView):
    model = Subject
    template_name = "subject_create.html"
    form_class = SubjectForm
    success_url = reverse_lazy("todo:subject_list")

class SubjectListView(generic.ListView):
    model = Subject
    template_name = "subject_list.html"

class SubjectUpdateView(generic.UpdateView):
    model = Subject
    template_name = "subject_update.html"

class SubjectDeleteView(generic.DeleteView):
    model = Subject
    template_name = "subject_delete.html"
    success_url = reverse_lazy("todo:subject_list")


class GlobalOverview(TemplateView):
    template_name = "global_overview.html"


class SubjectDetailView(generic.DetailView):
    template_name = "subject_details.html"
    model = Subject