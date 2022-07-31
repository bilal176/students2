from django.shortcuts import render
from home.models import students
from django.http.response import HttpResponseRedirect

# Create your views here.

def index(request):
    context ={'success':False }
    allTasks = students.objects.all()
    context2 ={'task':allTasks , 'success':False  }
    
  
    
    if request.method == "POST":
        name=request.POST.get('name')
        reg=request.POST.get('reg')
        sec=request.POST.get('sec')
        project_name=request.POST.get('project_name')
        project_field=request.POST.get('project_field')
        superident=request.POST.get('superident')
        Students = students(name=name , reg =reg ,sec=sec, project_name=project_name , project_field = project_field , superident=superident)
        Students.save()
        return HttpResponseRedirect('/')


        Students=students()
        context ={'success':True}
        context2 ={'task':allTasks , 'success':True  }
        

        
        
    return render(request, "add.html" ,  context2 )

def view(request):
    return render(request, "view.html")


def Task(request):
    allTasks = students.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.name)
    context ={'tasks':alltasks}
    return render(request, 'view.html' , context)