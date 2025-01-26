from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class ProductTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')

@register(Actor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio')

@register(Movie)
class ProductTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(Genre)
class ProductTranslationOptions(TranslationOptions):
    fields = ('genre_name',)