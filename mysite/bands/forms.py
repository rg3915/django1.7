from django import forms
from .models import Band, Member


class BandContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class BandForm(forms.ModelForm):

    class Meta:
        model = Band


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
