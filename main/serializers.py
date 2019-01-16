from rest_framework import serializers
from .models import Group, User


class MyUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'grupy')
        depth = 1


class MyGroupsSerializer(serializers.ModelSerializer):
    group_set = MyUsersSerializer(many=True)

    class Meta:
        model = Group
        fields = ('nazwa_grupy', 'group_set')
