from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Movie, Review, Comment

from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer



@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie= movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_delete_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk= review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data ={
            'message' : f'{review_pk}가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status= status.HTTP_202_ACCEPTED)

@api_view(['POST'])            
def comment_create(request, movie_pk, review_pk):
    serializer = CommentSerializer(data=request.data)
    review = get_object_or_404(Review, pk=review_pk)

    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET'])            
def comment_list(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
