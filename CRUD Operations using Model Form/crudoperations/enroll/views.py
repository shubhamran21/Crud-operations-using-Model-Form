from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User

# This function will add new item and show all items
def addandshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # if fm.is_valid():
        #      fm.save()  //this is also a method to add 
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stud':stud})
    
# This function will delete     

def delete(request, id):
  if request.method == 'POST':
      pi = User.objects.get(pk=id)    #pk is primary key 
      pi.delete()
      return HttpResponseRedirect('/')
  
# This function will update

def update(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
      fm.save()
    else:
      pi = User.objects.get(pk=id)
      fm = StudentRegistration(instance=pi)
    return render(request, 'updatestudent.html', {'form':fm})
    