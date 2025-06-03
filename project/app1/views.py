from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
# def landingPage(request):
#     # return HttpResponse("Hello world")
#     return HttpResponse("<h1>Hello world</h1>")

list1=[
     {"title":"title1","text":"Card-1 text","price":"US# 100"},
    {"title":"title2","text":"Card-2 text","price":"US# 200"},
  {"title":"title3","text":"Card-3 text","price":"US# 300"}
]

# def firstPageView(request):
#     return render(request,'first.html',{'name':"Python"})

def firstPageView(request):
    return render(request,'first.html',{'li':list1})

def secondPageView(request):
        return render(request,'second.html')

def landingPage(request):
    return render(request,'landing.html')

def pricingPage(request):
     return render(request,'pricing.html')

def pricingPage(request):
     return render(request,'pricing.html')

def pricingPage2(request):
     return render(request,'pricing2.html',{'li':list1})


def contactPage(request):
     #add code for form validation
     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
             print("Hi")
        else:
             print("Bye")
            
            


     return render(request,'contact.html')

#list1=[{"name":"Price1"},{"name2":"price2"},{"name3":"price3"}]

def indexPageView(request):
     return render(request,'index.html')



