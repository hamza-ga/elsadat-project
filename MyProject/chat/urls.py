from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from members import views  


urlpatterns = [
    path('', views.SignupPatientView.as_view(), name='signup'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]
