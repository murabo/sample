# -*- coding: utf-8 -*-
import datetime

from rest_framework import serializers

from app.models import Client, Like, Estimate


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('appoint_date', 'appoint_status')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('url', 'description', 'created_at')


class UserEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = (
            'estimate_id',
            'created_at',
            'site_id',
            'banquet_id',
            'guest_num',
            'style_id',
            'party_costume_id',
            'photo_id',
            'before_photo_id',
            'cuisine_id',
            'cake_flg',
            'movie_id',
            'coordinate_id',
            'effects',
            'date',
            'time'
        )

    effects = serializers.SerializerMethodField('effects_to_string')
    created_at = serializers.SerializerMethodField('created_at_to_timestamp')
    date = serializers.SerializerMethodField('created_at_to_timestamp')

    def effects_to_string(self, model):
        return ','.join(map(str,model.effect.select_related().values_list('id', flat=True)))

    def created_at_to_timestamp(self, model):
        return  int(
            datetime.datetime.combine(model.created_at, datetime.time()).timestamp()
        )

    def date_to_timestamp(self, model):
        return int(
            datetime.datetime.combine(model.date, datetime.time()).timestamp()
        )

    estimate_id=serializers.IntegerField(source='pk')
