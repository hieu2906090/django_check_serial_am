from django.shortcuts import render, redirect
from django.http import HttpResponse
from PagesApp.forms import NewEmForm, NewGDForm
from PagesApp.models import Employee, GiaoDich, GiaoDichDetail
from django.db.models import Count

def index(request):
    return render(request, 'pages/index.html')

############################## EMPLOYEE SECTION ################################
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


############################## TRANSACTION SECTION #############################
def list_transaction(request):
    tran_list = GiaoDich.objects.order_by('-create_date')
    tran_dict = {'trans': tran_list}
    return render(request, 'pages/trans/list_trans.html', context=tran_dict)

def transaction(request):
    tranForm = NewGDForm()
    if request.method == "POST":
        tranForm = NewGDForm(request.POST)
        if tranForm.is_valid():
            data = tranForm.save(commit=False)
            # data.quantity = data.to_serial - data.from_serial + 1
            data.save()
            return redirect('/trans/list')
        else:
            print('ERROR')
    return render(request, 'pages/trans/add_trans.html', {'form': tranForm})

def delete_trans(request, tran_id):
    GiaoDich.objects.get(id=tran_id).delete()
    return redirect('/trans/list')


######################### TRANSACTION DETAIL SECTION ###########################
def list_transaction_detail(request):
    tran_detail_list = GiaoDichDetail.objects.order_by('-create_date')
    td_dict = {'td': tran_detail_list}
    return render(request, 'pages/trans/list_detail.html', context=td_dict)


############################## DASHBOARD SECTION ###############################
def dashboard(request):
    em_count = Employee.objects.annotate(num_serial=Count('giaodichdetail'))
    count_dict = {'em': em_count}
    return render(request, 'pages/dash/dash_board.html', context=count_dict)

def list_trans_em(request, em_id):
    tran_detail_list = GiaoDichDetail.objects.filter(em_id=em_id).order_by('-create_date')
    td_dict = {'td': tran_detail_list}
    return render(request, 'pages/trans/list_detail.html', context=td_dict)