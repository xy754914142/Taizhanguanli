from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from .models import Taizhang,UserInfo
from utils.page import PageInfo
import openpyxl
from django.forms import Form
from django.forms import fields

class MyForm(Form):
    username = fields.CharField(
        max_length=16,
        min_length=6,
        required=True,
        error_messages={
            'max_length':'用户名长度应小于16位',
            'min_length':'用户名长度应大于6位',
            'required':'用户名不能为空',
        })
    password = fields.CharField(
        max_length=16,
        min_length=6,
        required=True,
        error_messages={
            'max_length':'密码长度应小于16位',
            'min_length':'密码长度应大于6位',
            'required':'密码不能为空',
        })

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        v = MyForm(request.POST)
        if v.is_valid():
            data = UserInfo.objects.filter(username=v.cleaned_data['username']).first()
            print(data.password)
            if v and data.password == v.cleaned_data['password']:
                    request.session['userinfo'] = {'username': v.cleaned_data['username'],
                                                   'password': v.cleaned_data['password']}
                    return redirect('/management.html')
            else:
                return render(request, 'login.html', {'erro': v.errors})
        else:
            return render(request,'login.html',{'erro':v.errors})

def login(func):
    def wrap(request, *args, **kwargs):
        if request.session.get('userinfo'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return wrap



@login
def logout(request):
    request.session.delete()
    return redirect('/login/')

def management(request):
    return render(request,'management.html')

class Update(View):
    def get(self,request):
        return render(request,'shebei_guanli/update.html')

    def post(self,request):
        file = request.FILES.get('date')
        excel_type = file.name.split('.')[1]
        if file is None:
            return HttpResponse("请选择需要上传的文件")
        if excel_type in ['xlsx','xls']:
            wb = openpyxl.load_workbook(file)
            for sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                for row in range(4,ws.max_row):
                    if(ws.cell(row=row, column=1).value != None and ws.cell(row=row, column=2).value != None):
                        date_list = []
                        for column in range(1, ws.max_column+1):
                            if(ws.cell(row=row, column=column).value != None):
                                date_list.append(ws.cell(row=row, column=column).value)
                        if(date_list):
                            try:

                                Taizhang.objects.create(
                                        device_name = date_list[0],
                                        device_model = date_list[1],
                                        device_range = date_list[2],
                                        device_precision = date_list[3],
                                        manufacturer = date_list[4],
                                        Commissioning_date = date_list[5],
                                        device_number = date_list[6],
                                        device_factory_number = date_list[7],
                                        calibration_department = date_list[8],
                                        calibration_cycle = date_list[9],
                                        calibration_time = date_list[10],
                                        expire_time = date_list[11],
                                        jieguo_type = date_list[12],
                                        device_type = date_list[13],
                                        device_user_department = date_list[14],
                                        node = date_list[15],
                                    )
                            except:
                                return HttpResponse('数据添加失败')


        return HttpResponse('OK')


def equipment_parameter(request,page):
    page_info = PageInfo(page, Taizhang.objects.all().count(), 10, '/equipment_parameter/', 11)
    class_list = Taizhang.objects.all()[page_info.start():page_info.end()]
    return render(request,'shebei_guanli/index.html',{'dates':class_list,'page_info':page_info})
