from django import forms
from .models import Rating


class RatingModelForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('content', 'score', )