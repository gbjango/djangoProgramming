# Generated by Django 3.2.8 on 2021-10-17 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dsuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '장고스타그램 사용자',
                'verbose_name_plural': '장고스타그램 사용자',
                'db_table': 'jangostar_dsuser',
            },
        ),
    ]
