# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Client, Like


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields = ('appoint_date', 'appoint_status')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Like
        fields = ('url', 'description', 'created_at')

