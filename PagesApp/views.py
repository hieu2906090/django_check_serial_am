from django.shortcuts import render, redirect
from django.http import HttpResponse
from PagesApp.forms import NewEmForm, NewGDForm
from PagesApp.models import Employee, GiaoDich, GiaoDichDetail
from django.db.models import Count

def index(request):
    return render(request, 'pages/index.html')

def employee(request):
    emForm = NewEmForm()
    if request.method == "POST":
        emForm = NewEmForm(request.POST)
        if emForm.is_valid():
            emForm.save(commit=True)
            return redirect('/employee/list')
        else:
            print('ERROR')
    return render(request, 'pages/em/add_employee.html', {'form': emForm})

def list_employee(request):
    em_list = Employee.objects.order_by('em_code')
    em_dict = {'em': em_list}
    return render(request, 'pages/em/list_employee.html', context=em_dict)

def edit_employee(request, em_id):
    em = Employee.objects.get(id=em_id)
    emForm = NewEmForm(instance=em)
    if request.method == "POST":
        emForm = NewEmForm(request.POST, instance=em)
        if emForm.is_valid():
            emForm.save(commit=True)
            return redirect('/employee/list')
        else:
            print('ERROR')
    return render(request, 'pages/em/add_employee.html', {'form': emForm})

def delete_employee(request, em_id):
    Employee.objects.get(id=em_id).delete()
    return redirect('/employee/list')

def transaction(request):
    tranForm = NewGDForm()
    if request.method == "POST":
        tranForm = NewGDForm(request.POST)
        if tranForm.is_valid():
            data = tranForm.save(commit=True)
            #add_transaction_detail(gd=data)
            return redirect('/trans/list')
        else:
            print('ERROR')
    return render(request, 'pages/trans/add_trans.html', {'form': tranForm})

def list_transaction_detail(request):
    tran_detail_list = GiaoDichDetail.objects.order_by('create_date')
    td_dict = {'td': tran_detail_list}
    return render(request, 'pages/trans/list_detail.html', context=td_dict)

def list_transaction(request):
    tran_list = GiaoDich.objects.order_by('create_date')
    tran_dict = {'trans': tran_list}
    return render(request, 'pages/trans/list_trans.html', context=tran_dict)

def dashboard(request):
    em_count = Employee.objects.annotate(num_serial=Count('giaodichdetail'))
    print(em_count)
    # GiaoDichDetail.objects.all().values('em_id').annotate(total=Count('em_id')).order_by('total')
    # count_dict = {'count': em_serial_count_list}
    # count_list = []
    # for i in em_serial_count_list:
    #     em = Employee.objects.get(id=i['em_id'])
    #     re = [em, i['total']]
    #     count_list.append(re)
    #     print(count_list)
    # print(count_list)
    count_dict = {'em': em_count}
    return render(request, 'pages/dash/dash_board.html', context=count_dict)

# def add_transaction_detail(gd):
#     for i in range(gd.from_serial, gd.to_serial+1):
#         try:
#             gd_detail = GiaoDichDetail(
#                 em_id_id = gd.em_id_id,
#                 gd_id_id = gd.id,
#                 status = 1,
#                 create_date = gd.create_date,
#                 serial = i
#             )
#             gd_detail.save()
#         except Exception as e:
#             print('Loi o serial: {0}'.format(i))
#             print(e)
#             continue
