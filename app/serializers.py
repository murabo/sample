# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields = ('last_name', 'first_name', 'full_name')
