from django import forms
from .models import Consaltations ,Prescription , Appointment
from datetimewidget.widgets import DateTimeWidget

class ConsaltationsForm(forms.ModelForm):
    disease_symptoms = forms.CharField(label = '', widget=forms.Textarea(attrs= {'class': 'field'}))
    photo = forms.ImageField(label = 'ارفع ملف', widget=forms.FileInput(attrs= {'class': 'form-control'}))
    class Meta:
        model = Consaltations
        fields = ('category','patient','doctor','disease_symptoms', 'photo')
        widgets = {
            'category': forms.TextInput(attrs= {'class': 'form-control' ,'value': '', 'id': 'category', 'type':'hidden' }),
            'patient': forms.TextInput(attrs= {'class': 'form-control','value': '', 'id': 'patient', 'type':'hidden' }),
            'doctor': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'doctor', 'type':'hidden' }),

        }   


class PrescriptionForm(forms.ModelForm):
    body = forms.CharField(label = 'اكتب الروشته', widget = forms.Textarea())
    class Meta:
        model = Prescription
        fields = ('doctor_name','patient_name','consult_id','body')
        widgets = {
            'doctor_name': forms.TextInput(attrs= {'class': 'form-control','value': '', 'id': 'doctor', 'type':'hidden' }),
            'patient_name': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'patient', 'type':'hidden' }),
            'consult_id': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'consult_id', 'type':'hidden' }),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
        }   


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(label = 'حدد ميعاد المقابله', widget = forms.SelectDateWidget())
    class Meta:
        model = Appointment
        fields = ('doc','pati', 'consultation_id','date')
        widgets = {
            'doc': forms.TextInput(attrs= {'id': 'doctor', 'type':'hidden' }),
            'pati': forms.TextInput( attrs= {'id': 'patient','type':'hidden' }),
            'consultation_id': forms.TextInput( attrs= {'id': 'consult_id', 'type':'hidden' }),
        }

class EditPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('body',)