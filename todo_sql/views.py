from django.shortcuts import render, redirect  # Не забудь redirect!
from .models import Task, Category
from .forms import TaskForm, CategoryForm # <--- 1. Импортируем нашу новую форму
from django.urls import reverse_lazy # Понадобится для переадресации
from django.views.generic import UpdateView, DeleteView , CreateView, ListView# Импортируем готовый класс-редактор
from django.views import View  # <--- Не забудь добавить этот импорт!
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

# (get_object_or_404 - это более безопасный способ сделать .get)



class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add.html'       # Нам понадобится простой шаблон
    success_url = reverse_lazy('index') # Куда вернуться после успеха


# 2. КЛАСС ПРОСМОТРА (Вместо функции index)
class TaskListView(ListView):


    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'  # Важно! Чтобы в HTML мы по-прежнему использовали имя 'tasks'

    # Настройка сортировки (аналог order_by)
    # Если в models.py есть ordering, эту строку можно не писать, но для надежности оставим:
    ordering = ['-created_at']




class TaskToggleView(View):
    def get(self, request, pk):
        # 1. Ищем задачу по PK (Primary Key = ID)
        task = Task.objects.get(id=pk)

        # 2. Меняем статус
        task.is_completed = not task.is_completed
        task.save()

        # 3. Уходим на главную
        return redirect('index')

    def toggle_task(request, task_id):
    # 1. Ищем задачу по ID

        task = Task.objects.get(id=task_id)

    # 2. Переворачиваем статус

        task.is_completed = not task.is_completed

    # 3. Сохраняем изменения в базу SQL
        task.save()

    # 4. Возвращаемся на главную
        return redirect('index')

    # def add_category(request):
    #     if request.method == 'POST':
    #         form = CategoryForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('index')
    #         else:
    #             form = CategoryForm()
    #         return render(request, 'add_category.html', {'form': form})

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index') # Куда вернуть после удаления
    template_name = 'delete.html'       # Шаблон с вопросом "Вы уверены?"


# Класс для редактирования
class TaskUpdateView(UpdateView):
    model = Task                    # 1. С какой моделью работаем?
    form_class = TaskForm           # 2. Какую форму используем?
    template_name = 'edit.html'     # 3. Какой HTML-шаблон показать?
    success_url = reverse_lazy('index') # 4. Куда перейти после успеха?

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('index') # Куда вернуться
