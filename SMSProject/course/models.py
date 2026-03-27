from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from student.models import Student
from professor.models import Professor

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from student.models import Student
from professor.models import Professor

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('enrolled', 'Enrolled'), ('completed', 'Completed'), ('dropped', 'Dropped')], default='enrolled')

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
