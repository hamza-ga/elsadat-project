from django.shortcuts import get_list_or_404, render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView , DetailView, UpdateView
from members.models import Doctor, Patient, Specialties
from pages.forms import ConsaltationsForm, PrescriptionForm, AppointmentForm , EditPrescriptionForm
from .models import Consaltations , Prescription, Appointment
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def view_doctor_profile(request,doc_pk):
    doctor = Doctor.objects.get(id = doc_pk)
    context = {'doctor': doctor}
    return render(request, 'pages/doctorprofile.html',context)


class EditPrescription(UpdateView):
    model = Prescription
    form_class = EditPrescriptionForm
    template_name = 'pages/editprescription.html'
    success_url = reverse_lazy('sucess')

class ShowAppointment(ListView):
    model = Appointment
    template_name = 'pages/showapoointment.html'

class AppointmentView(CreateView):
    form_class = AppointmentForm
    template_name = 'pages/createAppointment.html'
    success_url = reverse_lazy('sucess')

    def get_context_data(self, **kwargs):
        consult = get_object_or_404(Consaltations, id= self.kwargs['pk'])
        context = super(AppointmentView, self).get_context_data(**kwargs)
        context['patient_name'] = consult.patient.pk
        context['consult_id'] = consult.pk
        return context

class CreatePreConsult():
    pass

class ShowPreConsult(ListView):#patient view
    model = Prescription
    template_name = 'pages/showpreconsultation.html'

class ShowPrescription(DetailView):
    model = Prescription
    template_name = 'pages/showprescription.html'

    # def get_context_data(self, **kwargs):
    #     prescription = get_object_or_404(Prescription, doctor_name= self.kwargs['pk'])
    #     context = super(WritePrescriptionView, self).get_context_data(**kwargs)
    #     context['prescription'] = prescription
    #     return context



class ShowPrescriptionList(ListView):
    model = Prescription
    template_name = 'pages/showprescriptionlist.html'


class WritePrescriptionView(CreateView):
    model = Prescription
    form_class =  PrescriptionForm
    #fields = ('doctor_name','patient_name','body')
    template_name = 'pages/createprescript.html'
    success_url = reverse_lazy('sucess')

    def get_context_data(self, **kwargs):
        consult = get_object_or_404(Consaltations, id= self.kwargs['pk'])
        context = super(WritePrescriptionView, self).get_context_data(**kwargs)
        context['patient_name'] = consult.patient.pk
        context['consult_id'] = consult.pk
        return context



class ShowConsultsView(ListView):#doctor view
    model = Consaltations
    template_name = 'pages/showconsultslist.html'

    def get_context_data(self, **kwargs):
        consults = get_list_or_404(Consaltations, doctor= self.kwargs['pk'])
        context = super(ShowConsultsView, self).get_context_data(**kwargs)
        context['consults'] = consults
        return context   

class ShowConsultView(DetailView):#doctor view
    model = Consaltations
    template_name = 'pages/showconsultlist.html'



class ShowPreConsultsView(ListView):#doctor view
    model = Consaltations
    template_name = 'pages/showpreconsultslist.html'

    def get_context_data(self, **kwargs):
        consults = get_list_or_404(Consaltations, doctor= self.kwargs['pk'])
        context = super(ShowPreConsultsView, self).get_context_data(**kwargs)
        context['consults'] = consults
        return context   

class ShowPreConsultView(DetailView):#doctor view
    model = Consaltations
    template_name = 'pages/showpreconsultlist.html'


def getSugaryInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 3)
    context = {'dok_info': dok_info}
    return render(request, 'pages/spetializations_doctor.html', context)

def getCholesterolInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 1)
    context = {'dok_info': dok_info}
    return render(request, 'pages/spetializations_doctor.html', context)

def getPressureInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 2)
    context = {'dok_info': dok_info}
    return render(request, 'pages/spetializations_doctor.html', context)


class AddConsultation(CreateView):
    model = Consaltations
    form_class = ConsaltationsForm 
    template_name = 'pages/addconsultation.html'

        
    def get_context_data(self, **kwargs):
        doctor = get_object_or_404(Doctor, id= self.kwargs['pk'])
        context = super(AddConsultation, self).get_context_data(**kwargs)
        context['pk'] = doctor.pk
        context['c_pk'] = doctor.spcialty.pk
        return context


def sucess(request):
    context = {'x':'تمت العمليه بنجاح'}
    return render(request,'pages/success.html', context)
    