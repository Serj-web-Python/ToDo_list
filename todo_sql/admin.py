from django.contrib import admin
from .models import Task, Category  # Импортируем наш класс из соседнего файла

# Регистрируем модель в админке
admin.site.register(Task)
admin.site.register(Category)

