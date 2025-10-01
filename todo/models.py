from django.db import models
from django.db.models import PositiveIntegerField, ForeignKey
from django.utils.timezone import timezone, now

class Subject(models.Model):
    name = models.CharField(max_length=100)
    cp = models.PositiveIntegerField(default=0)
    class Status(models.IntegerChoices):
        NOT_TAKEN = 0, "Not taken"
        TAKEN = 1, "Taken"
        PASSED = 2, "Passed"
        DROPPED = 3, "Dropped"
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_TAKEN)
    have_exam_permit = models.BooleanField(default=False)
    exam_date = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    team = ForeignKey("Team", on_delete=models.CASCADE, null=True, blank=True)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    matriculation_number = PositiveIntegerField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name="students")

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    members = models.ManyToManyField(Student)

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)

    class Status(models.IntegerChoices):
        PENDING = 0, "Pending"
        IN_PROGRESS = 1, "In progress"
        COMPLETED = 2, "Completed"
        FAILED = 3, "Failed"
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)

    def how_far_ahead(self):
        if not self.deadline:
            return ""
        delta = self.deadline - now()
        if delta.total_seconds() < 0:
            return "Too late!"
        days = delta.days
        hours = delta.seconds // 3600
        return f"{days} days, {hours} hours"


class Subtask(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="subtasks")
    description = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    class Status(models.IntegerChoices):
        PENDING = 0, "Pending"
        IN_PROGRESS = 1, "In progress"
        COMPLETED = 2, "Completed"
    who_has_taken = models.CharField(max_length=100, blank=True)


