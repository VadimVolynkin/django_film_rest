from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', {"slug": self.url})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    name = models.CharField("Имя", max_length=150)
    image = models.ImageField("Изображение", upload_to="actors/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', {'slug': self.url})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание", null=True, blank=True)
    year = models.PositiveSmallIntegerField(default=1990)
    poster = models.ImageField("Постер", upload_to="movies/")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="film_genre")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True, related_name="film_category"
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('movie_detail', {"slug": self.url})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Review(models.Model):
    """ Отзывы """
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


