 
import os

import faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudprjct.settings')
import django
django.setup()

from testapp.models import employee
from faker import Faker
from random import *
faker=Faker()
 
#['eno','ename','esal','eadd']
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,30000)
        feadd=faker.city()
        emp_record=employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eadd=feadd)


         
         
n = int(input('Enter Number of Records:'))
populate(n)
print(f'{n} Records Inserted Succesfully')