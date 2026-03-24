from django import forms
from index.models import info


class infoForm(forms.Form):
    month = forms.IntegerField(
        max_value=12,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "The month:"
        })
    )

    date = forms.IntegerField(
        max_value=31,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "The day:"
        })
    )

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placholder": "Thing name"
        })
    )

    videoPhoto = forms.URLField(
        max_length=100,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "The link of video or photo:"
        })
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "rows": 5,
            "class": "form-control",
            "placeholder": "The description of the video:"
        })

    )

    credit = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placholder": "Author credit name:"
        })
    )