from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing API view"""
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
