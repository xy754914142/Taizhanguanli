# Generated by Django 3.1.6 on 2021-02-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shebei_guanli', '0002_auto_20210226_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meiyuewanchengshu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wancheng_1', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_1', models.IntegerField(default=0, max_length=168)),
                ('wancheng_2', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_2', models.IntegerField(default=0, max_length=168)),
                ('wancheng_3', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_3', models.IntegerField(default=0, max_length=168)),
                ('wancheng_4', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_4', models.IntegerField(default=0, max_length=168)),
                ('wancheng_5', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_5', models.IntegerField(default=0, max_length=168)),
                ('wancheng_6', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_6', models.IntegerField(default=0, max_length=168)),
                ('wancheng_7', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_7', models.IntegerField(default=0, max_length=168)),
                ('wancheng_8', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_8', models.IntegerField(default=0, max_length=168)),
                ('wancheng_9', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_9', models.IntegerField(default=0, max_length=168)),
                ('wancheng_10', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_10', models.IntegerField(default=0, max_length=168)),
                ('wancheng_11', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_11', models.IntegerField(default=0, max_length=168)),
                ('wancheng_12', models.IntegerField(default=0, max_length=168)),
                ('weiwancheng_12', models.IntegerField(default=0, max_length=168)),
                ('dangqianwanchengzongshu', models.IntegerField(default=0, max_length=382)),
            ],
        ),
    ]
