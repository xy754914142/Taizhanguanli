from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import openpyxl
# Create your views here.
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
                for row in range(1,ws.max_row):
                    for column in range(1, ws.max_column):
                        print(ws.cell(row=row, column=column).value)

        return HttpResponse('OK')
