from rest_framework import serializers


class AuthResponseSerializer(serializers.Serializer):
    authenticated = serializers.BooleanField()
    user = serializers.CharField()
    token = serializers.CharField(required=False, allow_null=True)
    method = serializers.CharField()
    headers = serializers.DictField()
    url = serializers.CharField()


class TokenValidationSerializer(serializers.Serializer):
    token = serializers.CharField()


class TokenValidationResponseSerializer(serializers.Serializer):
    valid = serializers.BooleanField()
    token = serializers.CharField()
    method = serializers.CharField()
    details = serializers.DictField(required=False)
