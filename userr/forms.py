from django import forms

from .models import Register,search,contact

class PageForm(forms.ModelForm):
    # phone = forms.CharField(disabled=True)
    class Meta:
        model=Register
        fields =[
            'name',
            'gender',
            'date_of_birth',
            'blood_group',
            'phone',
            'email',
            'area',
            'pincode',
            'city',
            'any_disease',
            ]

class User(forms.ModelForm):
    class Meta:
        model=search
        fields =['candidate_name',
                 'required_blood_group',
                 'purpose',
                 'pincode',
                 ]

class Message(forms.ModelForm):
    class Meta:
        model=contact
        fields =['name',
                 'email_id',
                 'message',
                 ]


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select blood group"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
    )
    blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
	    'placeholder':'A+/A-/B+/B-/O+/O-/AB+/AB-'
            },
            ),
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Address? Eg....Pune'
            }
        ),
    )

class Codeform(forms.Form):
    mobile=forms.CharField(label='Mobile number',help_text='Enter Mobile Number')
    otp=forms.CharField(label='Code',help_text='Enter SMS Verification Code',required=False)
    class Meta:
        fields=['mobile','otp']
    



