# -*- coding: utf-8 -*-
from django.db import models

from api.models import Banquet, Style, PartyCostume, Photo, BeforePhoto, Cuisine, Movie, Coordinate, Effect, Site


class Client(models.Model):
    first_name = models.CharField('姓', max_length=15)
    last_name = models.CharField('名', max_length=15)
    first_name_kana = models.CharField('セイ（Last kana）', max_length=30)
    last_name_kana = models.CharField('メイ（First kana）', max_length=30)
    tel = models.CharField('電話番号', max_length=15, null=True, default=None)
    mail = models.CharField('メール', max_length=15, null=True, default=None)
    place = models.ForeignKey(Site, verbose_name='会場名', on_delete=False)
    appoint_date = models.DateField('来館予定日', null=True, default=None)
    appoint_status = models.IntegerField('予約ステータス', choices=((0, '調整中'), (1, '確定'), (2, '会場')))
    link = models.CharField('リンク発行', max_length=15, null=True, default=None)
    site_id = models.CharField('会場ID', max_length=10, null=True, blank=True)
    test_type = models.CharField(
        'ABテストパターン(A/B)',
        choices=(("A", "A"), ("B", "B")),
        max_length=10,
        null=True, blank=True
    )

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
        verbose_name = '顧客情報'
        verbose_name_plural = '顧客情報'


class Like(models.Model):
    client = models.ForeignKey(Client, verbose_name='顧客', on_delete=False)
    url = models.CharField('URL', max_length=700)
    description = models.CharField('description', max_length=700)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.client.name, self.url)

    class Meta:
        db_table = 'like'
        verbose_name = 'お気に入り'
        verbose_name_plural = 'お気に入り'


class Estimate(models.Model):
    client = models.ForeignKey(Client, verbose_name='顧客', on_delete=False)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    site_id = models.CharField('会場ID', max_length=10, null=True, blank=True)
    banquet = models.ForeignKey(Banquet, verbose_name='バンケット', on_delete=False)
    guest_num = models.IntegerField("ゲスト人数")
    style = models.ForeignKey(Style, verbose_name='挙式スタイル', on_delete=False)
    party_costume = models.ForeignKey(PartyCostume, verbose_name='パーティ衣装スタイル', on_delete=False)
    photo = models.ForeignKey(Photo, verbose_name='フォト・記念撮影サービス', on_delete=False)
    before_photo = models.ForeignKey(BeforePhoto, verbose_name='前撮りサービス', on_delete=False)
    cuisine = models.ForeignKey(Cuisine, verbose_name='お料理', on_delete=False)
    cake_flg = models.BooleanField('ケーキ有無')
    movie = models.ForeignKey(Movie, verbose_name='記録ムービーサービス', on_delete=False)
    coordinate = models.ForeignKey(Coordinate, verbose_name='コーディネート', on_delete=False)
    effect = models.ManyToManyField(Effect, related_name='effects')
    date = models.DateField('希望日')
    time = models.IntegerField("0:AM / 1:PM", choices=((0, 'AM'), (1, 'PM'),))

    def __str__(self):
        return "{}: {}".format(self.client.name(), self.pk)

    class Meta:
        db_table = 'estimate'
        verbose_name = '見積もり情報'
        verbose_name_plural = '見積もり情報'
