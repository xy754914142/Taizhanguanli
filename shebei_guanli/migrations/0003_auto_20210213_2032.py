# Generated by Django 3.1.6 on 2021-02-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shebei_guanli', '0002_auto_20210213_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taizhang',
            name='calibration_cycle',
            field=models.CharField(max_length=64, verbose_name='检定周期'),
        ),
        migrations.AlterField(
            model_name='taizhang',
            name='calibration_department',
            field=models.CharField(max_length=64, verbose_name='检定部门'),
        ),
        migrations.AlterField(
            model_name='taizhang',
            name='device_type',
            field=models.CharField(default=0, max_length=64, verbose_name='设备类型'),
        ),
        migrations.AlterField(
            model_name='taizhang',
            name='device_user_department',
            field=models.CharField(default=1, max_length=64, verbose_name='所属部门'),
        ),
    ]
