from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment
from .forms import CourseForm, EnrollmentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {'form': form})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'course/course_detail.html', {'course': course, 'enrollments': enrollments})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/course_confirm_delete.html', {'course': course})

def enroll_student(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect('course_detail', pk=course_id)
    else:
        form = EnrollmentForm()
    return render(request, 'course/enroll.html', {'form': form, 'course': course})
