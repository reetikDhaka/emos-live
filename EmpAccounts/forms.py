from django import forms
from django.forms import fields, models, widgets
from .models import EmpData,WorkDonePerDay
class EmpForms(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style': 'height: 100px;'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Phone = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    #Department = forms.ModelChoiceField(widget=forms.ModelChoiceField(attrs={'class':'form-control'}))
    #empID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   
    def __init__(self, *args, **kwargs):
     super(EmpForms, self).__init__(*args, **kwargs)
     self.fields['Name'].widget.attrs['id']='employee-name'
     self.fields['Email'].widget.attrs['id']= 'email'
     self.fields['Phone'].widget.attrs['id']= 'phone-number'
     self.fields['Phone'].widget.attrs['class']='form-control'
     self.fields['Department'].widget.attrs['class']= 'btn btn-light'
     self.fields['Gender'].widget.attrs['class']= 'btn btn-light'

    class Meta:
        model = EmpData
        fields = '__all__'
        exclude = ('empID',)

class WorkDoneForm(forms.ModelForm):
    task_assignment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    #task_status = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    #task_assignment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(WorkDoneForm, self).__init__(*args, **kwargs)
        self.fields['attendance_date'].widget.attrs['class']='form-control'
        self.fields['employee'].widget.attrs['class']='form-control'


    
    class Meta:
        model = WorkDonePerDay
        fields = ('employee','task_assignment','attendance_date',)