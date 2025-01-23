import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORMproject.settings')
import django
django.setup()
from faker import Faker
from testapp.models import Employee
from random import*
Faker = Faker()
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = Faker.name()
        fesal = randint(10000,20000)
        feaddr = Faker.city()
        emp_record = Employee.objects.get_or_create(
            eno = feno,
            ename = fename,
            esal = fesal,
            eaddr = feaddr)
n = int(input('Enter number of Employees:'))
populate(n)
print('f{n} Records inserted successfully.....')