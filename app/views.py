# -*- coding:utf-8 -*-
from rest_framework import viewsets

from app.models import *
from app.serializers import PatientSerializer


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
