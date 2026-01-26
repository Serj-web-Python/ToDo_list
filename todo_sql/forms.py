from django import forms
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
