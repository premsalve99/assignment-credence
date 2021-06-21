from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length = None, use_url = True)
    class Meta:
        model = Movie
        fields = "__all__"
