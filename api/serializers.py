from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Link
        fields = ('id', 'orig_url', 'short_code', 'clicks', 'last_clicked', 'created_at')
        read_only_fields = ('id', 'short_code', 'clicks', 'last_clicked', 'created_at')

    def create(self, validated_data):
        return Link.objects.create(**validated_data)
    
