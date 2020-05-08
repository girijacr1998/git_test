
from django.shortcuts import render
from form1.form import NewUserForm

# Create your v

def index(request):
    return render(request,'form1/index.html')

def users(request):
    form =NewUserForm()

    if request.method=="POST":
      form =NewUserForm(request.POST)

      if form.is_valid():
          form.save(commit=True)
          return index(request)
      
      else:
          print("ERROR FORM INVALID")
  
    return render(request,'form1/users.html',{'form':form})