from django import forms
from matplotlib.pyplot import title
    
   


# Reordering Form and View

#class InputForm(forms.Form):



class PositionForm(forms.Form):
 
 title = forms.CharField()
 description = forms.CharField(max_length=200)
 complete = forms.BooleanField()
 start_time = forms.TimeField()
 end_time = forms.TimeField()
 duration = forms.DurationField()
 file_upload      = forms.FileField() 
 # position = forms.EmailField(max_length = 254)
 # position =  forms.DurationField()
 # position = forms.TimeField()


class InputForm(forms.Form):
    Username = forms.CharField()
    Email = forms.EmailField(max_length = 254)
    Password = forms.PasswordInput()
    
   # first_name = forms.CharField(max_length = 150)
    # last_name = forms.CharField(max_length = 150)

    
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    
    
    
"""

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
"""
    