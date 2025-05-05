from django import forms

from app.models import Person


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(choices={"Male": "Male", "Female": "Female"},widget=forms.RadioSelect)
    class Meta:
        model = Person
        fields = ['name', 'phone', 'email','dob','gender','height','weight',]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date','min':'1990-01-01', 'max':'2008-12-31'}),
            'weight': forms.NumberInput(attrs={'type': 'number','min':20, 'max':120}),
            'height': forms.NumberInput(attrs={'type': 'number','min':1.4, 'max':2.5}),

    }

#pip install django-crispy-forms
#pip install crispy-bootstrap5