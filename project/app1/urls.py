from django.urls import path
from .import views

urlpatterns=[
    path('',views.landingPage,name="LandingPage"),
    path('pricing',views.pricingPage,name="pricingPage"),
    path('pricing2',views.pricingPage2,name="pricingPage2"),
    path('contact',views.contactPage,name="contactPage"),
    path('first',views.firstPageView,name='firstPage'),
    path('second',views.secondPageView,name='secondPage'),
    path('index',views.indexPageView,name="indexPage")

]