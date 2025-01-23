from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
def retrieve_view(request):
    emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(ename__startswith='s')
    #emp_list = Employee.objects.filter(id__in=[1,3,5])
    #emp_list = Employee.objects.filter(ename__contains='Vijay')
    #emp_list = Employee.objects.filter(esal__gt=12000)
    #print(type(emp_list))  
    #emp_list = Employee.objects.filter(ename__endswith='s')
    #emp_list = Employee.objects.filter(esal__range=[12000,15000])
    #emp_list = Employee.objects.filter(ename__startswith='S') |Employee.objects.filter(esal__lt=12000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='A')|Q(esal__lt=11000))
    #emp_list = Employee.objects.filter(ename__startswith='S')&Employee.objects.filter(esal__lt=18000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='A')&Q(esal__lt=15000))
    #emp_list = Employee.objects.filter(ename__startswith='D',esal__lt=15000)
   # emp_list = Employee.objects.exclude(ename__startswith='D')

   # return render(request, 'testapp/index.html', {'emp_list': emp_list})
#def retrieve_view(request):
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #emp_list = Employee.objects.all().values('ename','esal')
    #emp_list = Employee.objects.all().only('ename','esal')
    return render(request,'testapp/specificcolumns.html',{'emp_list':emp_list})
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'],'max':max['esal__max'],
	'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/agggregate.html',my_dict)
