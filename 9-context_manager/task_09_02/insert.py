from create import BaseModel, Emails, Salary, Employees
from data import employees, emails, salary


for id, surname, name, fatherName in employees:
    Employees(surname=surname, name=name, fatherName=fatherName).save()
    
for id, empID, email in emails:
    Emails(empID=empID, email=email).save()
    
for empID, date, salaryType, amount in salary:
    Salary(empID=empID, date=date, salaryType=salaryType, amount=amount).save()

