from django.forms import ModelForm
from .models import Professor

#django model form class to create a professor registration form
class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        #fields = ['name', 'mob', 'email', 'department', 'college', 'specialization', 'experiance']
        fields = '__all__'