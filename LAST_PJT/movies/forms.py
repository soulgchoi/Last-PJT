from django import forms
from .models import Rating


class RatingModelForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Rating
        fields = ('content', 'score', )
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'})
        }