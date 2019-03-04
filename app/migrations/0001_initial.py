# Generated by Django 2.1.7 on 2019-03-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banquet_name', models.CharField(max_length=700, verbose_name='バンケット名')),
                ('banquet_description', models.CharField(max_length=700, verbose_name='バンケットの紹介文')),
                ('banquet_image', models.CharField(max_length=700, verbose_name='バンケットの画像')),
                ('banquet_base_cost', models.IntegerField(verbose_name='バンケットの基本費用')),
                ('banquet_cost_per_table', models.IntegerField(verbose_name='テーブル1卓当たりの費用')),
                ('banquet_cost_per_guest', models.IntegerField(verbose_name='ゲスト1人当たりの費用')),
                ('banquet_guest_per_table', models.IntegerField(verbose_name='テーブル1卓当たりのゲスト人数')),
                ('banquet_min_guests', models.IntegerField(verbose_name='対応可能な最小ゲスト人数')),
                ('banquet_max_guests', models.IntegerField(verbose_name='対応可能な最大ゲスト人数')),
            ],
            options={
                'verbose_name': 'バンケット',
                'verbose_name_plural': 'バンケット',
                'db_table': 'banquet',
            },
        ),
        migrations.CreateModel(
            name='BeforePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_photo_name', models.CharField(max_length=700, verbose_name='前撮りサービス名')),
                ('before_photo_description', models.CharField(max_length=700, verbose_name='前撮りサービスの紹介文')),
                ('party_costume_image', models.CharField(max_length=700, verbose_name='前撮りサービスの画像')),
                ('before_photo_cost', models.IntegerField(verbose_name='一式費用')),
            ],
            options={
                'verbose_name': '前撮りサービス',
                'verbose_name_plural': '前撮りサービス',
                'db_table': 'before_photo',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_cost', models.IntegerField(verbose_name='ウエディングケーキの基本費用')),
                ('cake_min_guest', models.IntegerField(verbose_name='このデータの金額になる最少人数')),
                ('cake_max_guest', models.IntegerField(verbose_name='このデータの金額になる最大人数')),
            ],
            options={
                'verbose_name': 'ウエディングケーキ',
                'verbose_name_plural': 'ウエディングケーキ',
                'db_table': 'cake',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='姓')),
                ('last_name', models.CharField(max_length=15, verbose_name='名')),
                ('first_name_kana', models.CharField(max_length=30, verbose_name='セイ（Last kana）')),
                ('last_name_kana', models.CharField(max_length=30, verbose_name='メイ（First kana）')),
                ('tel', models.CharField(default=None, max_length=15, null=True, verbose_name='電話番号')),
                ('mail', models.CharField(default=None, max_length=15, null=True, verbose_name='メール')),
                ('place', models.CharField(default=None, max_length=15, null=True, verbose_name='会場名')),
                ('appoint_date', models.DateField(default=None, null=True, verbose_name='来館予定日')),
                ('appoint_status', models.IntegerField(choices=[(0, '調整中'), (1, '確定')], verbose_name='予約ステータス')),
                ('link', models.CharField(default=None, max_length=15, null=True, verbose_name='リンク発行')),
                ('site_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='会場ID')),
                ('test_type', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=10, null=True, verbose_name='ABテストパターン(A/B)')),
            ],
            options={
                'verbose_name': '顧客情報',
                'verbose_name_plural': '顧客情報',
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate_name', models.CharField(max_length=700, verbose_name='コーディネート名')),
                ('coordinate_description', models.CharField(max_length=700, verbose_name='コーディネートの紹介文')),
                ('coordinate_image', models.CharField(max_length=700, verbose_name='コーディネートの画像')),
                ('coordinate_base_cost', models.IntegerField(verbose_name='基本費用')),
                ('coordinate_cost_per_guest', models.IntegerField(verbose_name='1卓当たりの費用')),
            ],
            options={
                'verbose_name': 'コーディネート',
                'verbose_name_plural': 'コーディネート',
                'db_table': 'coordinate',
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=700, verbose_name='お料理名')),
                ('cuisine_description', models.CharField(max_length=700, verbose_name='お料理の紹介文')),
                ('cuisine_image', models.CharField(max_length=700, verbose_name='お料理の画像')),
                ('cuisine_cost_per_guest', models.IntegerField(verbose_name='ゲスト1人当りの費用')),
            ],
            options={
                'verbose_name': 'お料理',
                'verbose_name_plural': 'お料理',
                'db_table': 'cuisine',
            },
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect_name', models.CharField(max_length=700, verbose_name='演出名')),
                ('effect_description', models.CharField(max_length=700, verbose_name='演出の紹介文')),
                ('effect_image', models.CharField(max_length=700, verbose_name='演出の画像')),
                ('effect_base_cost', models.IntegerField(verbose_name='全体の費用')),
                ('effect_cost_per_table', models.IntegerField(verbose_name='1卓当たりの費用')),
                ('effect_cost_per_guest', models.IntegerField(verbose_name='ゲスト1人当たりの費用')),
            ],
            options={
                'verbose_name': '演出',
                'verbose_name_plural': '演出',
                'db_table': 'effect',
            },
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('site_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='会場ID')),
                ('guest_num', models.IntegerField(verbose_name='ゲスト人数')),
                ('cake_flg', models.BooleanField(verbose_name='ケーキ有無')),
                ('date', models.DateField(verbose_name='希望日')),
                ('time', models.IntegerField(choices=[(0, 'AM'), (1, 'PM')], verbose_name='0:AM / 1:PM')),
                ('banquet', models.ForeignKey(on_delete=False, to='app.Banquet', verbose_name='バンケット')),
                ('before_photo', models.ForeignKey(on_delete=False, to='app.BeforePhoto', verbose_name='前撮りサービス')),
                ('client', models.ForeignKey(on_delete=False, to='app.Client', verbose_name='顧客')),
                ('coordinate', models.ForeignKey(on_delete=False, to='app.Coordinate', verbose_name='コーディネート')),
                ('cuisine', models.ForeignKey(on_delete=False, to='app.Cuisine', verbose_name='お料理')),
                ('effect', models.ManyToManyField(related_name='effects', to='app.Effect')),
            ],
            options={
                'verbose_name': '見積もり情報',
                'verbose_name_plural': '見積もり情報',
                'db_table': 'estimate',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=700, verbose_name='URL')),
                ('description', models.CharField(max_length=700, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('client', models.ForeignKey(on_delete=False, to='app.Client', verbose_name='顧客')),
            ],
            options={
                'verbose_name': 'お気に入り',
                'verbose_name_plural': 'お気に入り',
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=700, verbose_name='記録ムービーサービス名')),
                ('movie_description', models.CharField(max_length=700, verbose_name='記録ムービーサービスの紹介文')),
                ('movie_image', models.CharField(max_length=700, verbose_name='記録ムービーサービスの画像')),
                ('movie_cost', models.IntegerField(verbose_name='一式費用')),
            ],
            options={
                'verbose_name': '記録ムービーサービス',
                'verbose_name_plural': '記録ムービーサービス',
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='PartyCostume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_costume_name', models.CharField(max_length=700, verbose_name='パーティ衣装スタイル名')),
                ('party_costume_description', models.CharField(max_length=700, verbose_name='パーティ衣装スタイルの紹介文')),
                ('party_costume_image', models.CharField(max_length=700, verbose_name='パーティ衣装の画像')),
                ('party_costume_cost1', models.IntegerField(verbose_name='パーティ衣装スタイル種別が挙式スタイル種別と同じ場合の費用')),
                ('party_costume_cost2', models.IntegerField(verbose_name='パーティ衣装スタイル種別が挙式スタイル種別と違う場合の費用')),
                ('party_costume_type', models.IntegerField(choices=[(0, '和装'), (1, '洋装')], verbose_name='スタイル種別')),
            ],
            options={
                'verbose_name': 'パーティ衣装スタイル',
                'verbose_name_plural': 'パーティ衣装スタイル',
                'db_table': 'party_costume',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=700, verbose_name='フォト・記念サービス名')),
                ('photo_description', models.CharField(max_length=700, verbose_name='フォト・記念サービスの紹介文')),
                ('party_costume_image', models.CharField(max_length=700, verbose_name='フォト・記念サービスの画像')),
                ('photo_cost', models.IntegerField(verbose_name='一式費用')),
            ],
            options={
                'verbose_name': 'フォト・記念サービス',
                'verbose_name_plural': 'フォト・記念サービス',
                'db_table': 'photo',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=700, verbose_name='挙式スタイル名')),
                ('style_description', models.CharField(max_length=700, verbose_name='挙式スタイルの紹介文')),
                ('style_image', models.CharField(max_length=700, verbose_name='挙式スタイルの画像')),
                ('style_cost', models.IntegerField(verbose_name='費用')),
                ('style_type', models.IntegerField(choices=[(0, '和装'), (1, '洋装')], verbose_name='スタイル種別')),
            ],
            options={
                'verbose_name': '挙式スタイル',
                'verbose_name_plural': '挙式スタイル',
                'db_table': 'style',
            },
        ),
        migrations.AddField(
            model_name='estimate',
            name='movie',
            field=models.ForeignKey(on_delete=False, to='app.Movie', verbose_name='記録ムービーサービス'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='party_costume',
            field=models.ForeignKey(on_delete=False, to='app.PartyCostume', verbose_name='パーティ衣装スタイル'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='photo',
            field=models.ForeignKey(on_delete=False, to='app.Photo', verbose_name='フォト・記念撮影サービス'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='style',
            field=models.ForeignKey(on_delete=False, to='app.Style', verbose_name='挙式スタイル'),
        ),
    ]
