from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=[
            'judul',
            'body',
            'category',
        ]

        labels={
            'body':'Isi',
        }
        widgets={
            'judul': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'isi dengan judul artikel',
                }
            ),
             'body': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),

              'category': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
        }