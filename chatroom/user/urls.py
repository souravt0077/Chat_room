from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('register/',views.userRegister,name='register'),
    path('updateuser/',views.updateUser,name='updateuser'),

]
