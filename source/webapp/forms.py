from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class GuestbookForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='author')
    email = forms.EmailField(max_length=70, required=True, label='email')
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='status')