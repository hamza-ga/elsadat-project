from django.urls import path 
from . import  views

urlpatterns = [
    path('signup/', views.SignupPatientView.as_view(), name='signup'),
    path('edit-profile/', views.PatientEditView.as_view(),name = 'edit_profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change-password.html'),name = 'change_pass'),

]