from django.shortcuts import render
from .models import Course
from .forms import CourseForm
# Create your views here.

def upload_app(request):
    form_class = CourseForm
    context = {
        'form':form_class
    }
    return render(request,"upload/index.html",context) 

def upload(request):
    print("---------------")
    if request.method == 'POST':
        form = CourseForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    return render(request, 'upload/index.html', {'form': form})