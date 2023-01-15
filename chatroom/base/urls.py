from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('rooms/<str:pk>/',views.rooms,name='rooms'),
    path('createRoom/',views.createRoom,name='createroom'),
    path('updateRoom/<str:pk>/',views.updateRoom,name='updateroom'),
    path('deleteRoom/<str:pk>/',views.deleteRoom,name='deleteroom'),
    path('deleteMessage/<str:pk>/',views.deleteMessage,name='deletemessage'),
    path('moretopics/',views.moreTopics,name='moretopics'),
    path('usersprofile/<str:pk>/',views.userProfile,name='userprofile'),
]
