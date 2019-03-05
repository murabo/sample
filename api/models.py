# -*- coding: utf-8 -*-
from django.db import models


class Site(models.Model):
    site_name = models.CharField('会場名', max_length=700)

    def __str__(self):
        return self.site_name

    class Meta:
        db_table='site'
        verbose_name = '会場'
        verbose_name_plural = '会場'

class Banquet(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    banquet_name = models.CharField('バンケット名', max_length=700)
    banquet_description = models.CharField('バンケットの紹介文', max_length=700)
    banquet_image = models.CharField('バンケットの画像', max_length=700)
    banquet_base_cost = models.IntegerField('バンケットの基本費用')
    banquet_cost_per_table = models.IntegerField('テーブル1卓当たりの費用')
    banquet_cost_per_guest = models.IntegerField('ゲスト1人当たりの費用')
    banquet_guest_per_table = models.IntegerField('テーブル1卓当たりのゲスト人数')
    banquet_min_guests = models.IntegerField('対応可能な最小ゲスト人数')
    banquet_max_guests = models.IntegerField('対応可能な最大ゲスト人数')

    def __str__(self):
        return self.banquet_name

    class Meta:
        db_table = 'banquet'
        verbose_name = 'バンケット'
        verbose_name_plural = 'バンケット'


class Style(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    style_name = models.CharField('挙式スタイル名', max_length=700)
    style_description = models.CharField('挙式スタイルの紹介文', max_length=700)
    style_image = models.CharField('挙式スタイルの画像', max_length=700)
    style_cost = models.IntegerField('費用')
    style_type = models.IntegerField('スタイル種別', choices=((0, '和装'), (1, '洋装'),))

    def __str__(self):
        return self.style_name

    class Meta:
        db_table = 'style'
        verbose_name = '挙式スタイル'
        verbose_name_plural = '挙式スタイル'


class PartyCostume(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    party_costume_name = models.CharField('パーティ衣装スタイル名', max_length=700)
    party_costume_description = models.CharField('パーティ衣装スタイルの紹介文', max_length=700)
    party_costume_image = models.CharField('パーティ衣装の画像', max_length=700)
    party_costume_cost1 = models.IntegerField('パーティ衣装スタイル種別が挙式スタイル種別と同じ場合の費用')
    party_costume_cost2 = models.IntegerField('パーティ衣装スタイル種別が挙式スタイル種別と違う場合の費用')
    party_costume_type = models.IntegerField('スタイル種別', choices=((0, '和装'), (1, '洋装'),))

    def __str__(self):
        return self.party_costume_name

    class Meta:
        db_table = 'party_costume'
        verbose_name = 'パーティ衣装スタイル'
        verbose_name_plural = 'パーティ衣装スタイル'


class Photo(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    photo_name = models.CharField('フォト・記念サービス名', max_length=700)
    photo_description = models.CharField('フォト・記念サービスの紹介文', max_length=700)
    party_costume_image = models.CharField('フォト・記念サービスの画像', max_length=700)
    photo_cost = models.IntegerField('一式費用')

    def __str__(self):
        return self.photo_name

    class Meta:
        db_table = 'photo'
        verbose_name = 'フォト・記念サービス'
        verbose_name_plural = 'フォト・記念サービス'


class BeforePhoto(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    before_photo_name = models.CharField('前撮りサービス名', max_length=700)
    before_photo_description = models.CharField('前撮りサービスの紹介文', max_length=700)
    party_costume_image = models.CharField('前撮りサービスの画像', max_length=700)
    before_photo_cost = models.IntegerField('一式費用')

    def __str__(self):
        return self.before_photo_name

    class Meta:
        db_table = 'before_photo'
        verbose_name = '前撮りサービス'
        verbose_name_plural = '前撮りサービス'


class Cuisine(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    cuisine_name = models.CharField('お料理名', max_length=700)
    cuisine_description = models.CharField('お料理の紹介文', max_length=700)
    cuisine_image = models.CharField('お料理の画像', max_length=700)
    cuisine_cost_per_guest = models.IntegerField('ゲスト1人当りの費用')

    def __str__(self):
        return self.cuisine_name

    class Meta:
        db_table = 'cuisine'
        verbose_name = 'お料理'
        verbose_name_plural = 'お料理'


class Cake(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    cake_cost = models.IntegerField('ウエディングケーキの基本費用')
    cake_min_guest = models.IntegerField('このデータの金額になる最少人数')
    cake_max_guest = models.IntegerField('このデータの金額になる最大人数')

    def __str__(self):
        return self.cake_cost

    class Meta:
        db_table = 'cake'
        verbose_name = 'ウエディングケーキ'
        verbose_name_plural = 'ウエディングケーキ'


class Movie(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    movie_name = models.CharField('記録ムービーサービス名', max_length=700)
    movie_description = models.CharField('記録ムービーサービスの紹介文', max_length=700)
    movie_image = models.CharField('記録ムービーサービスの画像', max_length=700)
    movie_cost = models.IntegerField('一式費用')

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'movie'
        verbose_name = '記録ムービーサービス'
        verbose_name_plural = '記録ムービーサービス'


class Coordinate(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    coordinate_name = models.CharField('コーディネート名', max_length=700)
    coordinate_description = models.CharField('コーディネートの紹介文', max_length=700)
    coordinate_image = models.CharField('コーディネートの画像', max_length=700)
    coordinate_base_cost = models.IntegerField('基本費用')
    coordinate_cost_per_guest = models.IntegerField('1卓当たりの費用')

    def __str__(self):
        return self.coordinate_name

    class Meta:
        db_table = 'coordinate'
        verbose_name = 'コーディネート'
        verbose_name_plural = 'コーディネート'


class Effect(models.Model):
    site = models.ForeignKey(Site, verbose_name='会場', on_delete=False)
    effect_name = models.CharField('演出名', max_length=700)
    effect_description = models.CharField('演出の紹介文', max_length=700)
    effect_image = models.CharField('演出の画像', max_length=700)
    effect_base_cost = models.IntegerField('全体の費用')
    effect_cost_per_table = models.IntegerField('1卓当たりの費用')
    effect_cost_per_guest = models.IntegerField('ゲスト1人当たりの費用')

    def __str__(self):
        return self.effect_name

    class Meta:
        db_table = 'effect'
        verbose_name = '演出'
        verbose_name_plural = '演出'
