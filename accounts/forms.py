from django import forms
from .models  import Account

# create form for register page

# THIS IS A REGISTRAION FORM 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Enter Password",
        
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password"
    }))
    class Meta:
        model  = Account
        fields = ['first_name','last_name','phone_number','email','password']
        
    # applyin bootstrap form control class for all input of register for using loop through 
    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields["first_name"].widget.attrs['placeholder'] = 'First Name'
        self.fields["last_name"].widget.attrs['placeholder'] = 'Last Name'
        self.fields["email"].widget.attrs['placeholder'] = 'Email '
        self.fields["phone_number"].widget.attrs['placeholder'] = 'Phone Number'
       
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    def clean(self):
        cleaned_data     = super(RegistrationForm,self).clean()
        password         = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                'Password Does not match!'
            )