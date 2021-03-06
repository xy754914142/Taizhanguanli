# Generated by Django 3.1.6 on 2021-02-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A_Taizhang',
            fields=[
                ('device_name', models.CharField(blank=True, default='/', max_length=32, verbose_name='设备名称')),
                ('device_model', models.CharField(blank=True, default='/', max_length=64, verbose_name='设备型号')),
                ('device_range', models.CharField(blank=True, default='/', max_length=64, verbose_name='量程')),
                ('device_precision', models.CharField(blank=True, default='/', max_length=64, verbose_name='精度')),
                ('manufacturer', models.CharField(blank=True, default='/', max_length=64, verbose_name='制造商')),
                ('Commissioning_date', models.DateField(blank=True, null=True, verbose_name='启用日期')),
                ('device_number', models.CharField(blank=True, default='/', max_length=128, verbose_name='设备编号')),
                ('device_factory_number', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='本厂编号')),
                ('calibration_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定部门')),
                ('calibration_cycle', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定周期')),
                ('calibration_time', models.DateField(blank=True, null=True, verbose_name='检定日期')),
                ('expire_time', models.DateField(blank=True, null=True, verbose_name='到期日期')),
                ('jieguo_type', models.CharField(blank=True, default='合格', max_length=20, verbose_name='检定结果')),
                ('device_type', models.CharField(blank=True, default='A', max_length=64, verbose_name='设备类型')),
                ('device_user_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='所属部门')),
                ('node', models.CharField(blank=True, default='/', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='B_Taizhang',
            fields=[
                ('device_name', models.CharField(blank=True, default='/', max_length=32, verbose_name='设备名称')),
                ('device_model', models.CharField(blank=True, default='/', max_length=64, verbose_name='设备型号')),
                ('device_range', models.CharField(blank=True, default='/', max_length=64, verbose_name='量程')),
                ('device_precision', models.CharField(blank=True, default='/', max_length=64, verbose_name='精度')),
                ('manufacturer', models.CharField(blank=True, default='/', max_length=64, verbose_name='制造商')),
                ('Commissioning_date', models.DateField(blank=True, null=True, verbose_name='启用日期')),
                ('device_number', models.CharField(blank=True, default='/', max_length=128, verbose_name='设备编号')),
                ('device_factory_number', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='本厂编号')),
                ('calibration_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定部门')),
                ('calibration_cycle', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定周期')),
                ('calibration_time', models.DateField(blank=True, null=True, verbose_name='检定日期')),
                ('expire_time', models.DateField(blank=True, null=True, verbose_name='到期日期')),
                ('jieguo_type', models.CharField(blank=True, default='合格', max_length=20, verbose_name='检定结果')),
                ('device_type', models.CharField(blank=True, default='B', max_length=64, verbose_name='设备类型')),
                ('device_user_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='所属部门')),
                ('node', models.CharField(blank=True, default='/', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='BaoFei_Taizhang',
            fields=[
                ('device_name', models.CharField(blank=True, default='/', max_length=32, verbose_name='设备名称')),
                ('device_model', models.CharField(blank=True, default='/', max_length=64, verbose_name='设备型号')),
                ('device_range', models.CharField(blank=True, default='/', max_length=64, verbose_name='量程')),
                ('device_precision', models.CharField(blank=True, default='/', max_length=64, verbose_name='精度')),
                ('manufacturer', models.CharField(blank=True, default='/', max_length=64, verbose_name='制造商')),
                ('Commissioning_date', models.DateField(blank=True, null=True, verbose_name='启用日期')),
                ('device_number', models.CharField(blank=True, default='/', max_length=128, verbose_name='设备编号')),
                ('device_factory_number', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='本厂编号')),
                ('calibration_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定部门')),
                ('calibration_cycle', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定周期')),
                ('baofei_time', models.DateField(blank=True, null=True, verbose_name='报废日期')),
                ('jieguo_type', models.CharField(blank=True, default='合格', max_length=20, verbose_name='检定结果')),
                ('device_type', models.CharField(blank=True, default='B', max_length=64, verbose_name='设备类型')),
                ('device_user_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='所属部门')),
                ('node', models.CharField(blank=True, default='/', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='C_Taizhang',
            fields=[
                ('device_name', models.CharField(blank=True, default='/', max_length=32, verbose_name='设备名称')),
                ('device_model', models.CharField(blank=True, default='/', max_length=64, verbose_name='设备型号')),
                ('device_range', models.CharField(blank=True, default='/', max_length=64, verbose_name='量程')),
                ('device_precision', models.CharField(blank=True, default='/', max_length=64, verbose_name='精度')),
                ('manufacturer', models.CharField(blank=True, default='/', max_length=64, verbose_name='制造商')),
                ('Commissioning_date', models.DateField(blank=True, null=True, verbose_name='启用日期')),
                ('device_number', models.CharField(blank=True, default='/', max_length=128, verbose_name='设备编号')),
                ('device_factory_number', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='本厂编号')),
                ('calibration_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定部门')),
                ('calibration_cycle', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定周期')),
                ('calibration_time', models.DateField(blank=True, null=True, verbose_name='检定日期')),
                ('expire_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='到期日期')),
                ('jieguo_type', models.CharField(blank=True, default='合格', max_length=20, verbose_name='检定结果')),
                ('device_type', models.CharField(blank=True, default='C', max_length=64, verbose_name='设备类型')),
                ('device_user_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='所属部门')),
                ('node', models.CharField(blank=True, default='/', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='XianZhi_Taizhang',
            fields=[
                ('device_name', models.CharField(blank=True, default='/', max_length=32, verbose_name='设备名称')),
                ('device_model', models.CharField(blank=True, default='/', max_length=64, verbose_name='设备型号')),
                ('device_range', models.CharField(blank=True, default='/', max_length=64, verbose_name='量程')),
                ('device_precision', models.CharField(blank=True, default='/', max_length=64, verbose_name='精度')),
                ('manufacturer', models.CharField(blank=True, default='/', max_length=64, verbose_name='制造商')),
                ('Commissioning_date', models.DateField(blank=True, null=True, verbose_name='启用日期')),
                ('device_number', models.CharField(blank=True, default='/', max_length=128, verbose_name='设备编号')),
                ('device_factory_number', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='本厂编号')),
                ('calibration_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定部门')),
                ('calibration_cycle', models.CharField(blank=True, default='/', max_length=64, verbose_name='检定周期')),
                ('xianzhi_time', models.DateField(blank=True, null=True, verbose_name='闲置日期')),
                ('jieguo_type', models.CharField(blank=True, default='合格', max_length=20, verbose_name='检定结果')),
                ('device_type', models.CharField(blank=True, default='B', max_length=64, verbose_name='设备类型')),
                ('device_user_department', models.CharField(blank=True, default='/', max_length=64, verbose_name='所属部门')),
                ('node', models.CharField(blank=True, default='/', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
    ]
