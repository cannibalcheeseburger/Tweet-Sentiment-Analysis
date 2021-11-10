from django import forms

class TweetForm(forms.Form):
    text = forms.CharField(label='text', max_length=500)