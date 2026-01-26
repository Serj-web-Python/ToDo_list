from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



# Создаем Класс (Чертеж) задачи
class Task(models.Model):
    # 1. Текстовое поле (для названия задачи)
    # max_length=200 значит, что задача не может быть длиннее 200 букв
    title = models.CharField(max_length=200, verbose_name="Название задачи")

    # 2. Булево поле (галочка: сделано или нет)
    # default=False значит, что новая задача сразу будет "не сделанной"
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено?")

    # 3. Дата и время создания
    # auto_now_add=True значит "автоматически поставь текущее время в момент создания"
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    description = models.TextField(blank=True)
    objects = models.Manager

    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True,verbose_name="Категория")

    # Это магический метод.
    # Он говорит Django: "Когда будешь показывать эту задачу в админке, пиши её название, а не 'Task object (1)'"
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        # Если в конце нет восклицательного знака...
        if not self.title.endswith('!'):
            # ...добавляем его
            self.title = self.title + "!"

        # Выполняем настоящее сохранение
        super().save(*args, **kwargs)

    class Meta: #класс внутри класса, — это "наклейка на коробке", где написано,
        # как с этой посылкой обращаться. Здесь мы пишем настройки для самой модели.
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']


