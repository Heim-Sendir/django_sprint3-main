from django.db import models


class PublishedModel(models.Model):
    """Абстракстаня модель. Добавляет флаг is_published."""

    is_published = models.BooleanField(default=False,
                                       verbose_name='Опубликовано')


class TitleModel(models.Model):
    """Абстрактная модель. Добавляет поле title"""

    title = models.CharField(max_length=256, verbose_name='Заголовок')


class CreatedAtModel(models.Model):
    """Абстрактная модель. Добавляет поле created_at"""

    created_at = models.DateTimeField.auto_now()
