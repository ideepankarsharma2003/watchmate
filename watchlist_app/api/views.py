from django.shortcuts import render
from ..models import Movie
from .serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

# -----------------------------Normal Views--------------------------------

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies)
#     return JsonResponse({'movies': list(movies.values())})



# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     return JsonResponse({'movie': {
#         'name': movie.title,
#         'description': movie.description,
#         'active': movie.active
#     }})


# -----------------------------Function Based Views--------------------------------
# @api_view(['GET', 'POST', ])
# def movie_list(request):
#     if request.method=='GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     elif request.method=='POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
#         serializer= MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method=='PUT':
#         serializer= MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method=='DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'message': 'Movie deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# -----------------------------Class Based Views--------------------------------

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MovieDetail(APIView):
        
    def get(self, request, pk):
        try:
            movie= Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie= Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            movie= Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'message': 'Movie deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)