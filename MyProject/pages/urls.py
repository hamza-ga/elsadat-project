from django.urls import path 
from . import views



urlpatterns = [
    path('home/', views.home , name='home'),
    path('Sugary/', views.getSugaryInfo ,name = 'SugaryInfo'),
    path('Cholesterol/', views.getCholesterolInfo ,name = 'CholesterolInfo'),
    path('Pressure/', views.getPressureInfo ,name = 'PressureInfo'),
    path('addconsultation/<int:pk>/', views.AddConsultation.as_view() ,name = 'addconsultation'),
    path('sucess/', views.sucess , name = 'sucess'),
    path('show-consults/<int:pk>/', views.ShowConsultsView.as_view() , name = 'showconsults'),
    path('show-consult/<int:pk>/', views.ShowConsultView.as_view() , name = 'showconsult'),
    path('prescription-medicine/<int:pk>/', views.WritePrescriptionView.as_view() , name = 'prescription-medicine'),
    path('show-prescriptionlist/', views.ShowPrescriptionList.as_view() , name = 'show-prescriptionlist'),
    path('show-prescription/<int:pk>/', views.ShowPrescription.as_view() , name = 'show-prescription'),
    path('create-app/<int:pk>/', views.AppointmentView.as_view() , name = 'createappo'),
    path('show-app/', views.ShowAppointment.as_view() , name = 'showappo'),
    path('edit-prescription/<int:pk>/', views.EditPrescription.as_view() , name = 'editprescription'),
    path('view_doctor_profile/<int:doc_pk>/', views.view_doctor_profile , name = 'view_doctor_profile'),
]