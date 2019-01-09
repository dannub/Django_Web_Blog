from django.contrib.admin.widgets import AdminDateWidget
from django import forms


class ContactForm(forms.Form):
   nama_lengkap  = forms.CharField(
            label = 'Nama Lengkap',
            max_length = 20,
            widget = forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'masukkan nama lengkap anda',
                }
            )
   )
   jenis_kelamin = forms.ChoiceField(
       label="Jenis Kelamin",
       widget=forms.RadioSelect(
            attrs={
                    'class':'form-check-input',
                 }
       ),
       choices=[
           ('P','Pria'),
           ('W','Wanita'),
       ]
   )
   tanggal_lahir = forms.DateField(
       label = 'Tanggal Lahir',
       widget = forms.SelectDateWidget(
           attrs={
                    'class':' col-sm-2',
                 },
           years=range(1945,2019,1)
       )
   )
   email         = forms.EmailField(
       label = 'Email',
        widget = forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'masukkan email anda',
                }
            )
   )
   alamat        = forms.CharField(
       label = 'Alamat',
       widget=forms.Textarea(
           attrs = {
                    'class':'form-control',
                    'placeholder':'masukkan alamat lengkap anda',
                }
       )
    )
   agree         = forms.BooleanField(
        widget = forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                }
            )
   )