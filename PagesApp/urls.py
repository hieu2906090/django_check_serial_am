from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('dash', views.dashboard, name='dash'),
    path('employee/add', views.employee, name='add'),
    path('employee/list', views.list_employee, name='elist'),
    path('employee/edit/<int:em_id>', views.edit_employee),
    path('employee/delete/<int:em_id>', views.delete_employee),
    path('trans/add', views.transaction, name='tadd'),
    path('trans/detail', views.list_transaction_detail, name='dlist'),
    path('trans/list', views.list_transaction, name='tlist'),
    path('trans/delete/<int:tran_id>', views.delete_trans),
    path('trans/list/em/<int:em_id>', views.list_trans_em, name='etlist'),
]
