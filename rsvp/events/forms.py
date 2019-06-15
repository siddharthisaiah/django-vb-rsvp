from django import forms

class RsvpForm(forms.Form):
    rsvp = forms.BooleanField(label='RSVP ', required=False)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
