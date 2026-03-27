from django.shortcuts import redirect, render

from .models import Professor
from .forms import ProfessorForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()#storing the data in database using django model form
            return redirect('display')
    else:
        form = ProfessorForm()
        return render(request,'professor/register.html',{'form':form})

def display(request):
    #Logic to fetch the professors records from database 
    professors=Professor.objects.all()#fetching all records from Professor table
    return render(request,'professor/display.html',{'prof_objs':professors})