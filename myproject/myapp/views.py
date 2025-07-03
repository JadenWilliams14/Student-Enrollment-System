from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    # form_class = StudentForm
    fields = ['name', 'major', 'enrollment_date']
    template_name = 'myapp/student_form.html'
    success_url = reverse_lazy('myapp:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'myapp/student_form.html'
    fields = ['name', 'major', 'enrollment_date']
    success_url = reverse_lazy('myapp:student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    success_url = reverse_lazy('myapp:student_list')
