from django.urls import path
from  app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('add/',views.add,name='add'),
    path('display/',views.display,name='display'),
    path('remove/<int:pk>',views.remove,name='remove'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    
    path('logout/',views.logout,name='logout'),
    path('addf/<int:pk>',views.addf,name='addf'),
    path('attendence/',views.attendence,name='attendence'),
    path('branch/',views.branch,name='branch'),
    path('myattend/',views.myattend,name='myattend'),
    path('show/',views.show,name='show'),
    path('serch1/',views.serch1,name='serch1'),
    
    path('serch2/',views.serch2,name='serch2'),
    



    
   
]
