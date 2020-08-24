from rest_framework import serializers

from .models import Movie, Review, Actor




class FilterReviewListSerializer(serializers.ListSerializer):
    """ Фильтр комментариев только родители """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    """ Фильм комментариев рекурсивно дети """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class MovieListSerializer(serializers.ModelSerializer):
    """ Список Фильмов """

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'category')

class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerialiser(serializers.ModelSerializer):
    """ Вывод отзыва """
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = {'name', 'text', 'children'}


class ActorListSerializer(serializers.ModelSerializer):
    """ Вывод списка актеров и режиссеров """
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):
    """ Вывод актера и режиссера """
    class Meta:
        model = Actor
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    """ Полный фильм """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    actors = ActorListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewCreateSerializer(many=True)


    class Meta:
        model = Movie
        exclude = ('draft', )


