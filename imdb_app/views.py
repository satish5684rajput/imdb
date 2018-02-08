# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from imdb_app.serializers import MoviesSerializer
from django.db.models import Q

from .models import Movies


# Create your views here.
class RepoView(View):
    def get(self, request):
        movies = Movies.objects.all().prefetch_related('genre_type')
        return render(request, 'index.html', {'movies': movies})


# API views
@api_view(['GET', 'POST'])
def movie_list(request, format=None):
    """
    List all code movies, or create a new movie.
    """
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request_data = request.POST.copy()
        response = is_authenticated_user(request_data)
        if response == True:                
            serializer = MoviesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', "DELETE"])
def movie_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code movie.
    """
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        request_data = request.data.copy()
        response = is_authenticated_user(request_data)
        if response == True:
            serializer = MoviesSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response 

    elif request.method == 'DELETE':
        request_data = request.data.copy()
        response = is_authenticated_user(request_data)
        if response == True:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return response 


@api_view(['GET'])
def movie_search(request, search_term, format=None):
    """
    Search movie.
    """
    if request.method == 'GET':
        query_set = (
                    Q(movie_name__icontains=search_term) |
                    Q(director_name__icontains=search_term) |
                    Q(popularity_score__icontains=search_term) |
                    Q(imdb_score__icontains=search_term)
                )
        movies = Movies.objects.filter(query_set).distinct()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)


# user authenticate
def is_authenticated_user(request_data):
    try:
        username = request_data.get('username','')
        password = request_data.get('password','')
        user = authenticate(username=username, 
                            password=password)
        if not user:
            return Response({"Error": "User Not Found"}, 
                            status=status.HTTP_404_NOT_FOUND)            
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if user.is_superuser:                
        return True
    else:
        return Response({"Error": "User has no permission"}, 
                        status=status.HTTP_400_CREATED)