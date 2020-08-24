from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Movie, Actor
from .serializers import (MovieListSerializer,
                          MovieDetailSerializer,
                          ReviewCreateSerializer,
                          ActorListSerializer,
                          ActorDetailSerializer
                          )


class MovieListView(APIView):
    """ Вывод списка фильмов """
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """ Вывод фильма """

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

class ReviewCreateView(APIView):
    """ Вывод фильма """

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class ActorListView(generics.ListAPIView):
    """ Вывод списка актеров """
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    """ Вывод списка актеров """
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

