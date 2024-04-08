# Add any form classes for Flask-WTF here
from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    poster = forms.ImageField()

    def clean_poster(self):
        poster = self.cleaned_data.get('poster')
        if poster:
            if not poster.content_type.startswith('image'):
                raise forms.ValidationError("Only image files are allowed for the movie poster.")
        return poster