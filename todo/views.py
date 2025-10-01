from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView

from todo.forms import SubjectForm, AssignmentForm, AssignmentFormSet
from todo.models import Subject, Assignment


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
    form_class = SubjectForm

class SubjectDeleteView(generic.DeleteView):
    model = Subject
    template_name = "subject_delete.html"
    success_url = reverse_lazy("todo:subject_list")


class GlobalOverview(TemplateView):
    template_name = "global_overview.html"


class SubjectDetailView(generic.DetailView):
    template_name = "subject_details.html"
    model = Subject

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["assignment_list"] = Assignment.objects.filter(subject=self.object).order_by("deadline")
        return ctx

class AssignmentCreateView(generic.CreateView):
    model = Assignment
    template_name = "assignment_create.html"
    form_class = AssignmentForm

    def form_valid(self, form):
        subject = get_object_or_404(Subject, pk=self.kwargs['pk'])
        form.instance.subject = subject
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("todo:subject_details", kwargs={"pk": self.object.subject.pk})

class AssignmentsManageView(generic.UpdateView):
    model = Subject
    template_name = "assignments_update.html"
    fields = []

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if "formset" not in ctx:
            ctx["formset"] = self.get_formset()
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        formset = ctx["formset"]
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_formset(self, **kwargs):
        if self.request.method == "POST":
            return AssignmentFormSet(self.request.POST, instance=self.object, **kwargs)
        return AssignmentFormSet(instance=self.object, **kwargs)

    def get_success_url(self):
        return reverse("todo:subject_details", kwargs={"pk": self.object.pk})


