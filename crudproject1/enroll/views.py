from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data ['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em, password=pw)  
            reg.save()
            #fm.save()
        #fm=StudentRegistration(request.POST)

    else:
         fm=StudentRegistration(request.POST)
    stud=User.objects.all()

    return render(request,'enroll/add&show.html',{'form':fm,'stu':stud})

def delete_data(request,id):
    if request.method=='POST':
        dlt=User.objects.get(pk=id)
        dlt.delete()
        return HttpResponseRedirect('/')


def update_data(request,id):
    if request.method=='POST':
        upd=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=upd)
        if fm.is_valid():
            fm.save()
    else:
        upd=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=upd)        
    return render(request,'enroll/updateStudent.html',{'form':fm})

