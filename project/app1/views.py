from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm,StudentForm,RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

list1=[{"title":"title1","text":"Navigation available in Bootstrap share general markup and styles, from the base .nav class to the active and disabled states. Swap modifier classes to switch between each style","price":"US& 100"},
       {"title":"title1","text":"Card1","price":"US& 200"},
       {"title":"title1","text":"Card1","price":"US& 300"}]

def landingPage(request):
    return render(request,'landing.html')

def firstPageView(request):
    return render(request,'first.html',{"name":"Python","age":30,"li":list1})

def pricingPageView(request):
    return render(request,'pricing.html')

def pricingPageView2(request):
    return render(request,'pricing2.html',{"li":list1})

def contactPageView(request):
    form=ContactForm() 
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print("Hi")
            messages.success(request,"Response recorded")
        else:
            print("Bye")
            return render(request,'contact.html',{'form_data':form})
    return render(request,'contact.html',{'form_data':form})

def indexPageView(request):
    return render(request,'index.html')

def studentPageView(request):
    student_form=StudentForm()
    if request.method=='POST':
        
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            print("Form Accepted")
            
        else:
            print("Not Accepted")
            return render(request,'student.html',{'student_data':student_form})
    return render(request,'student.html',{'student_data':student_form})

def registerPageView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('loginPage')
    else:
        form = RegisterForm()  # This line ensures 'form' exists during GET requests

    return render(request, 'register.html', {'form': form})


def loginPageView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                # messages.success(request, "Login successful!")
                return redirect('dashboardPage')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def dashboardPageView(request):
    return render(request,'dashboard.html')

def logoutPageView(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect(loginPageView)


