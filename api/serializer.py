from django.contrib.auth.models import User

from rest_framework import serializers

# serializing user's data
class UserSeriarizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']