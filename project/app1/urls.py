from django.urls import path
from .import views

urlpatterns=[
    path('',views.landingPage,name="LandingPage"),
    path('pricing',views.landingPage,name="pricingPage"),
    path('pricing2',views.pricingPageView2,name="pricingPage2"),
    path('contact',views.contactPageView,name="contactPage"),
    path('first',views.firstPageView,name='firstPage'),
    path('second',views.pricingPageView,name='secondPage'),
    path('index',views.indexPageView,name="indexPage"),
    path('register',views.registerPageView,name="registerPage"),
    path('Student',views.studentPageView, name = "studentPage"),
    path('login',views.loginPageView,name='loginPage'),
    path('dashboard',views.dashboardPageView,name='dashboardPage'),
    path('logout',views.logoutPageView,name='logoutPage')


] 
