from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task,Category

class TaskForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Слишком коротко! Напиши подробнее.")
        return title

    class Meta:
        model = Task
        fields = ['title', 'description','category'] # Какие поля показать пользователю

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

# НОВАЯ ФОРМА ДЛЯ РЕГИСТРАЦИИ С EMAIL
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email адрес')  # Делаем поле обязательным

    class Meta:
        model = User
        fields = ['username', 'email']
