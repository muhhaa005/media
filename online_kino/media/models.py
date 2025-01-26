from http.cookiejar import reach

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, BooleanField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(75)], null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=64, default='simple')
    data_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=195, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    director_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(20), MaxValueValidator(100)], null=True,blank=True)
    director_image = models.ImageField(upload_to='director_images')

    def __str__(self):
        return f'{self.director_name}, {self.age}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(10), MaxValueValidator(99)])
    actor_image = models.ImageField(null=True, blank=True, upload_to='actor_images')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.actor_name}, {self.age}'


class Movie(models.Model):
    movie_name = models.CharField(max_length=32, unique=True)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1966), MaxValueValidator(2025)])
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_movie')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movie')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='actor_movie')
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='trailer_videos')
    movie_image = models.ImageField(upload_to='movie_images')
    status_movie = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.movie_name}, {self.year}, {self.director}'

class Types(models.Model):
    TYPES_CHOICES = (
        (144, 144),
        (360, 360),
        (480, 480),
        (720, 720),
        (1080, 1080
         ),
    )
    types = models.PositiveSmallIntegerField(choices=TYPES_CHOICES, default=720)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_types')

    def get_avg_rating(self):
        total = self.rating_movie.all()
        if total.exists():
            return round(sum([i.stars for i in total]) / total.count(), 1)

    def get_count_people(self):
        people = self.rating_movie.all()
        if people.exists():
            return people.count()
        return 0


class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)
    genre = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.genre_name

class GenreSimple(models.Model):
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True, related_name='director_genre')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='movie_genre')


class MovieLanguages(models.Model):
    language = models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_videos')
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name='language_movie')

    def __str__(self):
        return self.language


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='moment_photos', null=True, blank=True)

    def __str__(self):
        return self.movie


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating_movie')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'


class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart}, {self.movie}'


class History(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie}'

