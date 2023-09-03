from django.shortcuts import render
from .models import Teacher
from django.http import HttpResponseRedirect

def search_by_name(request):
    if request.method == 'POST':
        name = request.POST['name']
        teachers = Teacher.objects.filter(name__icontains=name)
        return render(request, 'search_results.html', {'teachers': teachers})
    return render(request, 'search_by_name.html')

def search_by_department(request):
    if 'department' in request.POST:
        department = request.POST.getlist('department')
        teachers = Teacher.objects.filter(department__in=department)
        return render(request, 'search_results.html', {'teachers': teachers})
    return render(request, 'search_by_department.html')
def search_results(request):
    teachers = Teacher.objects.all()
    return render(request, 'search_results.html', {'teachers': teachers})
def home(request):
    return render(request, 'home.html')