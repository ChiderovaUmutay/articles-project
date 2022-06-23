from django.db import models

# Create your models here.

STATUS_CHOICES = [('new', 'Новая'), ('moderated', 'Модерированная'), ('rejected', 'Отклоненная')]


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Cтатус", default=STATUS_CHOICES[0][0])

    def __str__(self):
        return f"{self.pk}.  {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
