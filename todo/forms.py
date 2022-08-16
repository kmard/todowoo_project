
from django.forms import ModelForm
from .models import Todo
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','memo','important']

class mTodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'css_input'}),label='Title')
    memo = forms.CharField(widget=forms.Textarea)
    important = forms.BooleanField(label='Important')
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

