# -*- coding: utf-8 -*-
import datetime

from rest_framework import serializers

from api.models import (
    Banquet, Style, PartyCostume, Photo,
    BeforePhoto, Cuisine, Cake, Movie,
    Coordinate, Effect
)


class BanquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banquet
        exclude = ('site',)


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        exclude = ('site',)


class PartyCostumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyCostume
        exclude = ('site',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = ('site',)


class BeforePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforePhoto
        exclude = ('site',)


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        exclude = ('site',)


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        exclude = ('site',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('site',)


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        exclude = ('site',)


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        exclude = ('site',)

