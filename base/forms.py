from django import forms
from .models import List_of_todo

class List_of_todoForms(forms.ModelForm):
    class Meta:
        model=List_of_todo
        fields=[
            'list_name','list_desc'
        ]