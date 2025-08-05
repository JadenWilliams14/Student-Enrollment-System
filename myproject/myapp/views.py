from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student

# Imports for Health Check
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class HealthCheckView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    # form_class = StudentForm
    fields = ['student', 'name', 'major', 'enrollment_date']
    template_name = 'myapp/student_form.html'
    success_url = reverse_lazy('students')
    # Automatically set owner on create (example)

    def form_valid(self, form):
        # Assuming your model has an 'owner' ForeignKey to User
        # Make sure 'owner' is NOT in the 'fields' attribute of the view
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    template_name = 'myapp/student_form.html'
    fields = ['name', 'major', 'enrollment_date']
    success_url = reverse_lazy('students')

    def test_func(self):
        return self.request.user.is_staff


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    fields = ['name', 'major', 'enrollment_date']
    success_url = reverse_lazy('students')

    def test_func(self):
        return self.request.user.is_staff
