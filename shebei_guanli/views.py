from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from .models import Taizhang,Userdate

import openpyxl
# Create your views here.
class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        userinfo = Userdate.objects.filter(username=user).first()

        if userinfo == None:
            return redirect(reverse('login'))
        if userinfo.password == pwd:
            cook = redirect(reverse('mian_html'))
            cook.set_signed_cookie('liu', 'fenglin', salt='abc', max_age=10000)
            return cook
        else:
            return redirect(reverse('login'))

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
                            else:
                                return HttpResponse('OK')


        return HttpResponse('OK')

class Equipment_parameter(View):
    def get(self,request):
        dates = Taizhang.objects.all()
        return render(request,'shebei_guanli/index.html',{'dates':dates})
