# Generated by Django 5.0.4 on 2024-05-04 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('userid', models.OneToOneField(db_column='userId', db_comment='ユーザーID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.user')),
                ('satisfieddate', models.DateTimeField(db_column='satisfiedDate', db_comment='フレンド成立日時')),
            ],
            options={
                'db_table': 'friend',
                'db_table_comment': 'フレンド情報',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Friendrequest',
            fields=[
                ('applicantid', models.OneToOneField(db_column='applicantId', db_comment='申請者ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.user')),
                ('applicantdate', models.DateTimeField(blank=True, db_column='applicantDate', db_comment='申請日時', null=True)),
            ],
            options={
                'db_table': 'friendrequest',
                'db_table_comment': 'フレンド申請',
                'managed': False,
            },
        ),
    ]