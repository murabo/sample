# -*- coding: utf-8 -*-
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
    appoint_status = models.IntegerField('予約ステータス', choices=((0, '調整中'), (1, '確定'),))
    link = models.CharField('リンク発行', max_length=15, null=True, default=None)
    site_id = models.CharField('会場ID', max_length=10, null=True, blank=True)
    test_type = models.CharField(
        'ABテストパターン(A/B)',
        choices=(("A", "A"), ("B","B")),
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

    class Meta:
        db_table = 'like'
        verbose_name = 'お気に入り'
        verbose_name_plural = 'お気に入り'


class Banquet(models.Model):
    banquet_name = models.CharField('バンケット名', max_length=700)
    banquet_description = models.CharField('バンケットの紹介文', max_length=700)
    banquet_image = models.CharField('バンケットの画像', max_length=700)
    banquet_base_cost = models.IntegerField('バンケットの基本費用')
    banquet_cost_per_table = models.IntegerField('テーブル1卓当たりの費用')
    banquet_cost_per_guest = models.IntegerField('ゲスト1人当たりの費用')
    banquet_guest_per_table = models.IntegerField('テーブル1卓当たりのゲスト人数')
    banquet_min_guests = models.IntegerField('対応可能な最小ゲスト人数')
    banquet_max_guests = models.IntegerField('対応可能な最大ゲスト人数')

    class Meta:
        db_table = 'banquet'
        verbose_name = 'バンケット'
        verbose_name_plural = 'バンケット'


class Style(models.Model):
    style_name = models.CharField('挙式スタイル名', max_length=700)
    style_description = models.CharField('挙式スタイルの紹介文', max_length=700)
    style_image = models.CharField('挙式スタイルの画像', max_length=700)
    style_cost = models.IntegerField('費用')
    style_type = models.IntegerField('スタイル種別', choices=((0, '和装'), (1, '洋装'),))

    class Meta:
        db_table = 'style'
        verbose_name = '挙式スタイル'
        verbose_name_plural = '挙式スタイル'


class PartyCostume(models.Model):
    party_costume_name = models.CharField('パーティ衣装スタイル名', max_length=700)
    party_costume_description = models.CharField('パーティ衣装スタイルの紹介文', max_length=700)
    party_costume_image = models.CharField('パーティ衣装の画像', max_length=700)
    party_costume_cost1 = models.IntegerField('パーティ衣装スタイル種別が挙式スタイル種別と同じ場合の費用')
    party_costume_cost2 = models.IntegerField('パーティ衣装スタイル種別が挙式スタイル種別と違う場合の費用')
    party_costume_type = models.IntegerField('スタイル種別', choices=((0, '和装'), (1, '洋装'),))

    class Meta:
        db_table = 'party_costume'
        verbose_name = 'パーティ衣装スタイル'
        verbose_name_plural = 'パーティ衣装スタイル'


class Photo(models.Model):
    photo_name = models.CharField('フォト・記念サービス名', max_length=700)
    photo_description = models.CharField('フォト・記念サービスの紹介文', max_length=700)
    party_costume_image = models.CharField('フォト・記念サービスの画像', max_length=700)
    photo_cost = models.IntegerField('一式費用')

    class Meta:
        db_table = 'photo'
        verbose_name = 'フォト・記念サービス'
        verbose_name_plural = 'フォト・記念サービス'


class BeforePhoto(models.Model):
    before_photo_name = models.CharField('前撮りサービス名', max_length=700)
    before_photo_description = models.CharField('前撮りサービスの紹介文', max_length=700)
    party_costume_image = models.CharField('前撮りサービスの画像', max_length=700)
    before_photo_cost = models.IntegerField('一式費用')

    class Meta:
        db_table = 'before_photo'
        verbose_name = '前撮りサービス'
        verbose_name_plural = '前撮りサービス'


class Cuisine(models.Model):
    cuisine_name = models.CharField('お料理名', max_length=700)
    cuisine_description = models.CharField('お料理の紹介文', max_length=700)
    cuisine_image = models.CharField('お料理の画像', max_length=700)
    cuisine_cost_per_guest = models.IntegerField('ゲスト1人当りの費用')

    class Meta:
        db_table = 'cuisine'
        verbose_name = 'お料理'
        verbose_name_plural = 'お料理'


class Cake(models.Model):
    cake_cost = models.IntegerField('ウエディングケーキの基本費用')
    cake_min_guest = models.IntegerField('このデータの金額になる最少人数')
    cake_max_guest = models.IntegerField('このデータの金額になる最大人数')

    class Meta:
        db_table = 'cake'
        verbose_name = 'ウエディングケーキ'
        verbose_name_plural = 'ウエディングケーキ'


class Movie(models.Model):
    movie_name = models.CharField('記録ムービーサービス名', max_length=700)
    movie_description = models.CharField('記録ムービーサービスの紹介文', max_length=700)
    movie_image = models.CharField('記録ムービーサービスの画像', max_length=700)
    movie_cost = models.IntegerField('一式費用')

    class Meta:
        db_table = 'movie'
        verbose_name = '記録ムービーサービス'
        verbose_name_plural = '記録ムービーサービス'


class Coordinate(models.Model):
    coordinate_name = models.CharField('コーディネート名', max_length=700)
    coordinate_description = models.CharField('コーディネートの紹介文', max_length=700)
    coordinate_image = models.CharField('コーディネートの画像', max_length=700)
    coordinate_base_cost = models.IntegerField('基本費用')
    coordinate_cost_per_guest = models.IntegerField('1卓当たりの費用')

    class Meta:
        db_table = 'coordinate'
        verbose_name = 'コーディネート'
        verbose_name_plural = 'コーディネート'


class Effect(models.Model):
    effect_name = models.CharField('演出名', max_length=700)
    effect_description = models.CharField('演出の紹介文', max_length=700)
    effect_image = models.CharField('演出の画像', max_length=700)
    effect_base_cost = models.IntegerField('全体の費用')
    effect_cost_per_table = models.IntegerField('1卓当たりの費用')
    effect_cost_per_guest = models.IntegerField('ゲスト1人当たりの費用')

    class Meta:
        db_table = 'effect'
        verbose_name = '演出'
        verbose_name_plural = '演出'


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

    class Meta:
        db_table = 'estimate'
        verbose_name = '見積もり情報'
        verbose_name_plural = '見積もり情報'
