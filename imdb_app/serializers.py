from imdb_app.models import Movies, Genre
from rest_framework import serializers



class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)


class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    genre_type = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movies
        fields = ('id', 'movie_name', 'director_name', 'popularity_score', 
                    'imdb_score', 'genre_type')


