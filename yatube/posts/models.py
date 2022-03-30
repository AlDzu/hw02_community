from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Путь', unique=True)
    description = models.TextField('Oписание', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группы'


class Post(models.Model):
    text = models.TextField('Текст поста',)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Посты'
        ordering = ('-pub_date',)
