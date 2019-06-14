from django import forms

class RsvpForm(forms.Form):
    rsvp = forms.BooleanField(label='RSVP ', required=False)
