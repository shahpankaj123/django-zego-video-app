from django.urls import path
from vapp import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path('signup/',views.signup,name='signup'),
    path('Logout/',views.Logout,name='logout'),
    path('home/',views.home,name='home'),
    path('join',views.videomeet,name='meet'),
    path('joinmeeting',views.joinmeet,name='joinmeet')
]