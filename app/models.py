# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    last_name = models.CharField('名字', max_length=10)
    first_name = models.CharField('名前', max_length=10)

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        db_table = 'patient'


class Client(models.Model):
    first_name = models.CharField('姓', max_length=15)
    last_name = models.CharField('名', max_length=15)
    first_name_kana = models.CharField('セイ（Last kana）', max_length=30)
    last_name_kana = models.CharField('メイ（First kana）', max_length=30)
    tel = models.CharField('電話番号', max_length=15, null=True, default=None)
    mail = models.CharField('メール', max_length=15, null=True, default=None)
    place = models.CharField('会場名', max_length=15, null=True, default=None)
    date = models.DateField('来館予定日', null=True, default=None)
    link= models.CharField('リンク発行', max_length=15, null=True, default=None)
    k = models.Transform


    def name(self):
        return self.last_name + self.first_name


    def kana(self):
        return self.last_name_kana + self.first_name_kana

    name.short_description = '氏名'
    kana.short_description = 'フリガナ'

    class Meta:
        db_table = 'client'
        verbose_name='顧客情報'
        verbose_name_plural = '顧客情報'
