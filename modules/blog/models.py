from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from modules.services.utils import *
from .choice import *

User = get_user_model()


class Subject(MPTTModel):
    """
    Категории со вложенностью
    """
    subject_name = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    descript = models.TextField(max_length=300, verbose_name='Описание')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория')

    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('subject_name',)

    class Meta:
        """
        Сортировка, название в админ панели, таблица с данными
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('posts_by_subject', kwargs={'slug': self.slug})


class City(models.Model):
    city_name = models.CharField(max_length=100)
    city_region = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Region(models.Model):
    region_name = models.CharField(max_length=100)


class Post(models.Model):
    """
    Модель постов для сайта
    """

    class PostManager(models.Manager):
        def all(self):
            return self.get_queryset().filter(status='draft')

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, blank=True, unique=True, verbose_name='Альт.название')
    subject = TreeForeignKey(Subject, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, verbose_name='Город')
    content = models.TextField(max_length=300, verbose_name='Описание')
    date_posted = models.DateTimeField(default=timezone.now)
    cost = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    view = models.IntegerField(verbose_name='Просмотры')
    thumbnail = models.ImageField(
        verbose_name='Превью',
        blank=True,
        upload_to='images/thumbnails/%Y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    status = models.CharField(choices=AnnouncmentState.CHOICES, default=AnnouncmentState.draft, max_length=10)
    objects = PostManager()
    """liked = models.ManyToManyField(User, default=None, blank=True)"""

    class Meta:
        ordering = ['-date_posted']
        indexes = [models.Index(fields=['-date_posted', 'status'])]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)
