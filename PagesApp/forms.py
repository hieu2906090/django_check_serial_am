from django import forms
from PagesApp.models import Employee, GiaoDich, GiaoDichDetail
import datetime

class NewEmForm(forms.ModelForm):
    em_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nhập tên nhân viên ...'
        }
    ))

    em_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nhập mã nhân viên ...'
        }
    ))

    STATUS = [(1,'Hoạt động'), (2,'Không hoạt động')]
    status = forms.ChoiceField(choices=STATUS, widget=forms.RadioSelect(
        attrs={
            'class': 'radio',
        }
    ))

    em_create_date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget())

    class Meta():
        model = Employee
        fields = ('em_name', 'em_code', 'status', 'em_create_date')

class NewGDForm(forms.ModelForm):
    from_serial = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nhập Serial từ ...'
        }
    ))

    to_serial = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nhập Serial đến ...'
        }
    ))

    em = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    status = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    create_date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget(years=range(2015, 2030)))

    class Meta():
        model = GiaoDich
        fields = ('from_serial', 'to_serial', 'em', 'create_date', 'status')
