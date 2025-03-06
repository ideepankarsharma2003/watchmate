from django.urls import path, include

# from .views import movie_list, movie_detail # Function Based Views
from .views import MovieList, MovieDetail # Class Based Views

urlpatterns = [
    # Function Based Views
    # path('list/', movie_list, name='movie-list'),
    # path('detail/<int:pk>/', movie_detail, name='movie-detail'), 

    # Class Based Views
    path('list/', MovieList.as_view(), name='movie-list'),
    path('detail/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
]
