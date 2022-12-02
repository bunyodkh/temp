from django import forms

from .models import Consultant


class ConsultantlForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = [
            'first_name', 
            'last_name', 
            'middle_name', 
            'age', 
            'sex', 
            'image', 
            'email',
            'phone',
            'daily_fee', 
            'type', 
            'experience', 
            'education',
            'spheres', 
            'competence', 
            'competences',
        ]
        
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'input-field'}),
            'last_name' : forms.TextInput(attrs={'class': 'input-field'}),
            'middle_name' : forms.TextInput(attrs={'class': 'input-field'}),
            'age': forms.NumberInput(attrs={'class': 'input-field'}),
            'sex': forms.Select(attrs={'class': 'input-field'}),
            'image': forms.FileInput(attrs={'class': 'input-field'}),

            'daily_fee' : forms.NumberInput(attrs={'class': 'input-field'}),            
            'email' : forms.TextInput(attrs={'class': 'input-field'}),
            'phone' : forms.TextInput(attrs={'class': 'input-field'}),
            'type': forms.Select(attrs={'class': 'input-field'}),

            'education' : forms.Textarea(attrs={'class': 'input-field'}),
            'experience' : forms.Textarea(attrs={'class': 'input-field'}),
            'competences': forms.SelectMultiple(attrs={'class': 'input-field'}),
            'competence' : forms.Textarea(attrs={'class': 'input-field'}),
            'spheres': forms.SelectMultiple(attrs={'class': 'input-field'}),

        }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'middle_name': 'Middle name',
        }

        # error_messages = {
        #     'link': {
        #         'max_length': _("Максимальная длина линка 500 символов. Больше низьзя!"),
        #     },
        #     'description' : {
        #         'max_length': _("Попробуйте сократить текст!"),
        #     }
        # }