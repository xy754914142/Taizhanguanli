# Generated by Django 3.1.6 on 2021-02-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shebei_guanli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='abstract',
            field=models.CharField(max_length=168, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default='默认用户', max_length=32),
        ),
    ]
