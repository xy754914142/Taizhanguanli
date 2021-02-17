from django.db import models

# Create your models here.
class Userdate(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)



class Taizhang(models.Model):
    # calibration_department_choice = (
    #     (0,'公司'),
    #     (1,'特种'),
    #     (2,'宜昌'),
    #     (3,'宜都'),
    #     (4,'广东'),
    #     (5,'广电'),
    # )
    # calibration_time_choice = (
    #     (0,'半年'),
    #     (1,'1年'),
    #     (2,'2年'),
    # )
    # device_type_choice = (
    #     (0, 'B类'),
    #     (1, 'A类'),
    #     (2, 'C类'),
    # )
    # device_user_department_choice = (
    #     (0, '设备科'),
    #     (1, '环保科'),
    #     (2, '生产计划科'),
    #     (3, '信息科'),
    #     (4, '技术科'),
    #     (5, '质量科'),
    # )

    device_name = models.CharField(max_length=32,verbose_name='设备名称')
    device_model = models.CharField(max_length=64,verbose_name='设备型号')
    device_range = models.CharField(max_length=64,verbose_name='量程')
    device_precision = models.CharField(max_length=64,verbose_name='精度')
    manufacturer = models.CharField(max_length=64,verbose_name='制造商')
    Commissioning_date = models.DateField(null=True, blank=True, verbose_name='启用日期')
    device_number = models.CharField(max_length=128,verbose_name='设备编号')
    device_factory_number = models.CharField(primary_key=True,max_length=128,unique=True,verbose_name='本厂编号')

    calibration_department = models.CharField(max_length=64,verbose_name='检定部门')
    calibration_cycle = models.CharField(max_length=64,verbose_name='检定周期')

    # calibration_department = models.SmallIntegerField(choices=calibration_department_choice,default=0,verbose_name='检定部门')
    # calibration_cycle = models.SmallIntegerField(choices=calibration_department_choice,default=1,verbose_name='检定周期')

    calibration_time = models.DateField(null=True, blank=True, verbose_name='检定日期')
    expire_time = models.DateField(null=True, blank=True, verbose_name='到期日期')
    jieguo_type = models.CharField(max_length=20, verbose_name='检定结果')

    # device_type = models.SmallIntegerField(choices=device_type_choice, default=0, verbose_name='设备类型')
    # device_user_department = models.SmallIntegerField(choices=device_user_department_choice, default=1, verbose_name='所属部门')

    device_type = models.CharField(max_length=64, default=0, verbose_name='设备类型')
    device_user_department = models.CharField(max_length=64, default=1,verbose_name='所属部门')
    node = models.CharField(max_length=128,null=True, verbose_name='备注')