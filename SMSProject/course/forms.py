from django import forms
from .models import Course, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter course description', 'rows': 4}),
            'professor': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'