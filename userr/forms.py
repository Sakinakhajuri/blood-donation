from django import forms

from .models import Register,search,contact

class PageForm(forms.ModelForm):
    date_of_birth = forms.CharField(help_text='Date as : YYYY-MM-DD')
    last_blood_donated_date = forms.CharField(help_text='Date as : YYYY-MM-DD',required=False)
    aadhar_no =forms.CharField(min_length=12,max_length=12)
    phone = forms.CharField(min_length=13, max_length=13)
    class Meta:
        model=Register
        fields =[
            'name',
            'gender',
            'date_of_birth',
            'blood_group',
            'phone',
            'email',
            'aadhar_no',
            'area',
            'pincode',
            'city',
            'last_blood_donated_date',
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



class Codeform(forms.Form):
    mobile=forms.CharField(label='Mobile number',help_text='Enter Mobile Number along with country code')
    otp=forms.CharField(label='Code',help_text='Enter SMS Verification Code',required=False)
    class Meta:
        fields=['mobile','otp']
    
class UpdateDonate(forms.Form):
    name = forms.CharField(max_length=100)
    aadhar_no = forms.CharField(min_length=12, max_length=12)
    new_donated_date = forms.CharField(help_text='Date as : YYYY-MM-DD')
    class Meta:
        fields=['name','aadhar_no','new_donated_date']


class UpdateLoc(forms.Form):
    name = forms.CharField(max_length=100)
    aadhar_no = forms.CharField(min_length=12, max_length=12)
    updated_area = forms.CharField(max_length=100)
    updated_city= forms.CharField(max_length=100)
    updated_pincode = forms.IntegerField()
    class Meta:
        fields=['name','aadhar_no','updated_area','updated_city','updated_pincode']


