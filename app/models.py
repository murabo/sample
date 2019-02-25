# -*- coding: utf-8 -*-
from django.db import models


class Patient(models.Model):
    last_name = models.CharField('名字', max_length=10)
    first_name = models.CharField('名前', max_length=10)

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        db_table = 'patient'
