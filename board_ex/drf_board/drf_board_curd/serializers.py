from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer): #list
    class Meta:
        model = Board
        fields = ('id', 'author', 'title') 



class BoardDetailSerializer(serializers.HyperlinkedModelSerializer): # detail
    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'content')
