from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),


]