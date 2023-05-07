from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    """Модель, описывающая категории произведений."""
    name = models.CharField(max_length=255, verbose_name=('Категория'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=('URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')


class Genre(models.Model):
    """Модель, описывающая жанры произведений."""
    name = models.CharField(max_length=100, verbose_name=('Название'))
    slug = models.SlugField(unique=True, verbose_name=('URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Title(models.Model):
    """Модель, описывающая произведения."""
    name = models.CharField(max_length=100, verbose_name=('Название'))
    year = models.IntegerField(verbose_name=('Год выпуска'))
    description = models.TextField(
        null=True, blank=True, verbose_name=('Описание'))
    genre = models.ManyToManyField(
        Genre, related_name='title', verbose_name=('URL жанра'))
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='title',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name', 'description']


class Review(models.Model):
    """Модель, описывающая отзыв на произведение."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель, описывающая комментарии к отзывам."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
