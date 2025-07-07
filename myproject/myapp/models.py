from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
# Create your models here.


class Student(models.Model):
    student = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    major = models.CharField(max_length=50)
    enrollment_date = models.DateField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
        related_name='%(class)s_items'
    )

    # Added save logic because I was running into null error when creating new student's as the id would not auto-populate
    def save(self, *args, **kwargs):
        if self.student is None:
            last_student = Student.objects.order_by('student').last()
            if last_student:
                self.student = last_student.student + 1
            else:
                self.student = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.name} - {self.major} - {self.enrollment_date}"


class Course(models.Model):
    course = models.CharField(primary_key=True, max_length=6)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)])

    def __str__(self):
        return f"{self.course} - {self.course_name} - {self.credits}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.CharField(max_length=11)
    grade = models.DecimalField(decimal_places=2, max_digits=5,
                                validators=[MaxValueValidator(100.00), MinValueValidator(0.00)])

    class Meta:
        unique_together = ('semester', 'student', 'course')

    def __str__(self):
        return f"{self.semester} - {self.student} - {self.course} - {self.grade}"


class Instructor(models.Model):
    instructor = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.instructor} - {self.name} - {self.department}"


class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True)
    schedule = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.class_id} - {self.course.course_name} - {self.instructor.name} - {self.schedule}"
