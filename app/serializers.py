from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["long_url", "short_url", "clicks"]
        read_only_fields = ["short_url", "clicks"]