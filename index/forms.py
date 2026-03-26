from django import forms
from index.models import info
import calendar


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

    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get('month')
        date = cleaned_data.get('date')

        if month > 12:
            raise ValueError("Months can't be larger than 12")
        
        if date > 31:
            raise ValueError("Date can't be larger than 31")
        
        if month == 2 & date > 29:
            raise ValueError("Date can't be larger than 29")
            
        

        

        return cleaned_data
    
    def save(self):
        cleaned_data = self.cleaned_data

        info.objects.create(
            month=cleaned_data.get("month"),
            date=cleaned_data.get("date"),
            name=cleaned_data.get("name"),
            videoPhoto=cleaned_data.get("videoPhoto"),
            description=cleaned_data.get("description"),
            credit=cleaned_data.get("credit"),
        )
    
    