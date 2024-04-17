from django import forms

class CommentForm(forms.Form):
    """Form to handle commenting"""
    heading = forms.CharField(max_length=150)
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols":"30"}))

