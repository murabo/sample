# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    first_name = models.CharField('姓', max_length=15)
    last_name = models.CharField('名', max_length=15)
    first_name_kana = models.CharField('セイ（Last kana）', max_length=30)
    last_name_kana = models.CharField('メイ（First kana）', max_length=30)
    tel = models.CharField('電話番号', max_length=15, null=True, default=None)
    mail = models.CharField('メール', max_length=15, null=True, default=None)
    place = models.CharField('会場名', max_length=15, null=True, default=None)
    appoint_date = models.DateField('来館予定日', null=True, default=None)
    appoint_status = models.IntegerField('予約ステータス', choices=((0,'調整中'),(1,'確定'),))
    link= models.CharField('リンク発行', max_length=15, null=True, default=None)
    site_id = models.CharField('会場ID', max_length=10, null=True, blank=True)
    test_type = models.CharField('ABテストパターン(A/B)', max_length=10, null=True, blank=True)


    def name(self):
        return self.last_name + self.first_name


    def kana(self):
        return self.last_name_kana + self.first_name_kana

    name.short_description = '氏名'
    kana.short_description = 'フリガナ'

    def __str__(self):
        return self.last_name + self.first_name

    class Meta:
        db_table = 'client'
        verbose_name='顧客情報'
        verbose_name_plural = '顧客情報'


class Like(models.Model):
    client = models.ForeignKey(Client, verbose_name='顧客', on_delete=False)
    url=models.CharField('URL', max_length=700)
    description=models.CharField('description', max_length=700)
    created_at = models.DateTimeField(u'登録日時', auto_now_add=True)
