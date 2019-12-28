from django import forms
from .models import TaiKhoang

class TaiKhoangForm(forms.ModelForm):
    class Meta:
        model = TaiKhoang
        fields = ['question_text']
        labels = {'question_text': 'Your text'}

# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['choice_text']
#         labels = {'choice_text': 'Your choice'}
#         widgets = {'choice_text': forms.Textarea(attrs={'cols':80})}
