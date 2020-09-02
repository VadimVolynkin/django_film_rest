from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView


from .models import Movie, Actor
from .serializers import (MovieListSerializer,
                          MovieDetailSerializer,
                          ReviewCreateSerializer,
                          ActorListSerializer,
                          ActorDetailSerializer,
                          )


class MovieListView(ListAPIView):
    """ Вывод списка фильмов """
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieListSerializer
    pagination_class = PageNumberPagination


class MovieDetailView(APIView):
    """ Вывод фильма """

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """ Написать отзыв """

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class ActorListView(ListAPIView):
    """ Вывод списка актеров """

    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(RetrieveAPIView):
    """ Вывод актера """

    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

