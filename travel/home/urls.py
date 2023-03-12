from django.urls import path
from home import views


 


urlpatterns = [
    
    path('',views.loginUser,name = "login"),
    path('home',views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name='contact'),
    path('Services',views.Services,name = 'Services'),
    path('Course',views.Course,name = 'Course'),
    path('upload',views.upload,name = 'uplaod'),
    path('Dbms',views.Dbms,name = 'Dbms'),
    path('texRec',views.texRec,name='texRec'),
    

]


# STATICFILES_DIRS
 
