# Generated by Django 5.0.4 on 2024-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(db_column='ID', db_comment='チャットルーム識別用ID', primary_key=True, serialize=False)),
                ('roomname', models.CharField(db_comment='ルーム名', max_length=255)),
            ],
            options={
                'db_table': 'chatroom',
                'db_table_comment': 'チャットルーム',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roominfo',
            fields=[
                ('id', models.IntegerField(db_comment='ルーム情報ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'roominfo',
                'db_table_comment': 'チャットルーム情報',
                'managed': False,
            },
        ),
    ]
