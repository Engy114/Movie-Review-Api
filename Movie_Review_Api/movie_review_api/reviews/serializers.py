from rest_framework import serializers
from .models import User
from .models import Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie_id', 'rating', 'comment', 'user']
