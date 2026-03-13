from django import forms


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

    video = forms.URLField(
        max_length=100,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "The name:"
        })
    )

