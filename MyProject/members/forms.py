from django.contrib.auth.forms import UserCreationForm , UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import  Patient , Specialties


class SignUpPatientForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'ذكر'),
        ('F', 'انثى'),
    )
    BLOOD_TYPES = (
        ('A+','A+'),
        ('A-','A-'),
        ('B-','B-'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB-','AB-'),
        ('AB+','AB+')
    )
    username = forms.CharField(label = 'اسم المستخدم' )
    email = forms.EmailField(label = 'البريد الاكتروني' ,widget=forms.EmailInput(attrs= {'class': 'field'}))
    first_name = forms.CharField(label = 'الاسم الاول', widget=forms.TextInput(attrs= {'class': 'field'}))
    last_name = forms.CharField(label = 'الاسم الثاني', widget=forms.TextInput(attrs= {'class': 'field'}))
    password1 = forms.CharField(label = 'كلمة السر', widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'اعد كتابة كلمة السر', widget = forms.PasswordInput())
    birthday = forms.DateField(label = 'تاريخ الميلاد', widget=forms.SelectDateWidget(attrs= {'class': 'field'}))
    phone_number = forms.CharField(label = 'رقم التليفون', widget=forms.TextInput(attrs= {'class': 'field'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES ,label = 'النوع', widget=forms.Select(attrs= {'class': 'gender field'}))
    blood = forms.ChoiceField(choices=BLOOD_TYPES, label = 'فصيلة الدم', widget=forms.Select(attrs= {'class': 'kind field'}))
    city = forms.CharField(label = 'الدوله', widget=forms.TextInput(attrs= {'class': 'field'}))

    class Meta:
        model = Patient
        fields = ('username','first_name','last_name','email','password1','password2','gender','blood','city' ,'birthday','phone_number')
        # widgets = {
        #     'disease' : forms.Select()
        # }
    
    def __init__(self, *args, **kwargs):
        super(SignUpPatientForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs= {'class': 'form-control'}
        self.fields['password1'].widget.attrs= {'class': 'form-control'}
        self.fields['password2'].widget.attrs= {'class': 'form-control'}



class EditPatientForm(UserChangeForm):
    GENDER_CHOICES = (
        ('M', 'ذكر'),
        ('F', 'انثى'),
    )
    BLOOD_TYPES = (
        ('A+','A+'),
        ('A-','A-'),
        ('B-','B-'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB-','AB-'),
        ('AB+','AB+')
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'class': 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES ,label = 'النوع', widget=forms.Select(attrs= {'class': 'gender field'}))
    blood = forms.ChoiceField(choices=BLOOD_TYPES, label = 'فصيلة الدم', widget=forms.Select(attrs= {'class': 'kind field'}))
    city = forms.CharField(label = 'الدوله', widget=forms.TextInput(attrs= {'class': 'field'}))

    class Meta:
        model = Patient
        fields = ('first_name','last_name','email','password' ,'birthday','phone_number', 'gender', 'blood', 'city')


class EditDoctortForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    spcialty = forms.CharField(max_length=50, widget=forms.Select(attrs= {'class': 'form-control'}))
    

    class Meta:
        model = Patient
        fields = ('username','first_name','last_name','email','password','spcialty')

