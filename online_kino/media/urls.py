from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profile_list')
router.register(r'moment', MomentsViewSet, basename='moment_list')


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),

    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),

    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),

    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),

    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),

    path('language/', MovieLanguagesListAPPIView.as_view(), name='language_list'),
    path('language/<int:pk>/', MovieLanguagesDetailAPIView.as_view(), name='language_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list'}), name='favorite_list'),
    path('favorite_movie/', FavoriteMovieViewSet.as_view({'get': 'list', 'delete': 'destroy'}), name='favorite_movie_list'),
    path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'list'}), name='favorite_movie_detail'),

    path('rating/', RatingCreateAPIView.as_view(), name='rating_create'),

    path('history/', HistoryViewSet.as_view({'get': 'list'}), name='history_list'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]