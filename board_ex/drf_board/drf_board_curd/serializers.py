from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer): #list
    class Meta:
        model = Board
        fields = ('id', 'author', 'title') 

    # author 필드 검증
    def validate_author(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("author는 5글자 이상이어야 합니다.")
        return value

    # title 필드 검증
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("title은 5글자 이상이어야 합니다.")
        return value


class BoardDetailSerializer(serializers.HyperlinkedModelSerializer): # detail
    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'content')

    # author 필드 검증
    def validate_author(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("author는 5글자 이상이어야 합니다.")
        return value

    # title 필드 검증
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("title은 5글자 이상이어야 합니다.")
        return value
    
    # content 필드 검증
    def validate_content(self, value):
        if len(value) > 20:
            raise serializers.ValidationError("content는 20글자 이하로 작성해야 합니다.")
        return value