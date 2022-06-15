from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpPatientForm , EditPatientForm ,EditDoctortForm
from .models import Patient , Doctor

# Create your views here.

class SignupPatientView(generic.CreateView):
    model = Patient
    form_class = SignUpPatientForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('sucess')

class PatientEditView(generic.UpdateView):
    model = Patient
    form_class = EditPatientForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('sucess')
    def get_object(self):
        return self.request.user

class DoctorEditView(generic.UpdateView):
    model = Doctor
    form_class = EditDoctortForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('sucess')

    def get_object(self):
        return self.request.user