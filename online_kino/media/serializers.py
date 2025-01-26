from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'username', 'age', 'phone_number', 'status', 'data_registered']

class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']

class CountrySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializer(serializers.ModelSerializer):
    director_country = CountrySimpleSerializer()
    class Meta:
        model = Director
        fields = ['id', 'director_name', 'director_image', 'director_country']

class DirectorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'actor_name', 'actor_image']

class ActorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']

class GenreSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['id', 'language']

class MovieLanguagesSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language']


class MovieListSerializer(serializers.ModelSerializer):
    language_movie = MovieLanguagesSimpleSerializer(many=True, read_only=True)
    movie_genre = GenreSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'movie_time', 'movie_genre', 'language_movie']


class DirectorDetailSerializer(serializers.ModelSerializer):
    director_movie = MovieListSerializer(many=True, read_only=True)
    director_country = CountrySimpleSerializer()
    director_genre = GenreSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['director_name', 'director_image', 'director_country', 'bio', 'age', 'director_movie', 'director_genre']


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovieListSerializer(many=True, read_only=True)
    country = CountryListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_image','bio', 'age', 'country', 'actor_movie']


class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_movie']

class CountryDetailSerializer(serializers.ModelSerializer):
    country_movie = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name']


class RatingSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'created_date', 'text']

class RatingCrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    rating_movie = RatingSerializer(many=True, read_only=True)
    director = DirectorSimpleSerializer()
    actor = ActorSimpleSerializer()
    country = CountrySimpleSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField
    movie_genre = GenreSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'director', 'actor', 'country', 'movie_genre',
                  'types', 'movie_time', 'year', 'description', 'movie_image', 'movie_trailer',
                  'status_movie', 'rating_movie', 'avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class MovieLanguagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['id', 'movie', 'movie_moments']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True, source='movie')
    class Meta:
        model = FavoriteMovie
        fields =['id', 'cart', 'movie', 'movie_id']


class FavoriteSerializer(serializers.ModelSerializer):
    favorite = FavoriteMovieSerializer(many=True, read_only=True)
    class Meta:
        model = Favorite
        fields = ['user', 'favorite']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['movie', 'viewed_at']

