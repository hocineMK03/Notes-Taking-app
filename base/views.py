from django.shortcuts import render,redirect
from .models import List_of_todo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import List_of_todoForms
# Create your views here.
user1=None

def home(request):
    isauthenticated=False
    user1=request.user
    print(isauthenticated)
    if user1 is not None:
        isauthenticated=True

    print(isauthenticated)
    print(user1)
    context={
        'isauthenticated':isauthenticated,
        'user1':request.user}
    return render(request,'home.html',context)

def login_page(request):
    page=True
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        try:
            user=User.objects.get(username=username)
        except:
            return redirect('home')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            user1=user
            return redirect('notes')


    context={'page':page}
    return render(request,'login_and_register.html',context)

def register_page(request):
    page=False
    usercreation=UserCreationForm()
    if request.method=='POST':
        usercreation=UserCreationForm(request.POST)
        if usercreation.is_valid():
            user=usercreation.save(commit=False)
            user.save()
            login(request,user)
            return redirect('notes')
    context={
        'usercreation':usercreation,
        'page':page
    }
    return render(request,'login_and_register.html',context)


def notes(request):
    list_of_todo1 = List_of_todo.objects.filter(host=request.user).order_by('-date_created')
    latest5=list_of_todo1.order_by('-date_created')[:5]
    context={
        'listoftodo':list_of_todo1,
        'latest5':latest5
    }
    return render(request,'notes.html',context)
def list_create(request):
    form=List_of_todoForms()
    if request.method=='POST':
        form=List_of_todoForms(request.POST)
        if form.is_valid:
            notesaved=List_of_todo.objects.create(
                host=request.user,
                list_name=request.POST.get('list_name'),
                list_desc=request.POST.get('list_desc')


            )
            return redirect('notes')
    
    context={'form':form}
    return render(request,'list_create.html',context)


def logout1(request):
    logout(request)
    return render(request,'home.html')


def note_delete(request,pk):
    note_for_delete=List_of_todo.objects.get(id=pk)
    note_for_delete.delete()
    return redirect('notes')
   

