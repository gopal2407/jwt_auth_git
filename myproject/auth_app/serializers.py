from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

    def create(self, valiated_data):
        return User.objects.create_user(**valiated_data)

