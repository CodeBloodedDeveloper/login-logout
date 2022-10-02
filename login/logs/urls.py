from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello), 
    
    path('', views.signup, name= 'signup'), 
    path('login/', views.userlogin, name= 'userlogin'), 
    path('logout/', views.logout, name= 'logout'), 
    path('portfolio/', views.portfolio, name= 'portfolio'),

    
]
