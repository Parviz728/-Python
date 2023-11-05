from peewee import fn, Case, JOIN
from create import Emails, Salary, Employees

query = (Employees
         .select(
             Employees.id.alias('id'),
             (Employees.surname + ' ' + Employees.name + ' ' + Employees.fatherName).alias('FIO'),
             fn.AVG(
                 Case(None, [(Salary.salaryType == 'salary', Salary.amount)], None)
             ).alias('Avg_salary'),
             fn.AVG(
                 Case(None, [(Salary.salaryType == 'bonus', Salary.amount)], None)
             ).alias('Avg_bonus'),
             (Emails.email + ' ').alias('email')
         )
         .join(Salary, on=(Employees.id == Salary.empID))
         .join(Emails, JOIN.LEFT_OUTER, on=(Employees.id == Emails.empID))
         .where(fn.date_part('year', Salary.date) == 2020)
         .group_by(Employees.id, Employees.surname, Employees.name, Employees.fatherName, Emails.email)
         .order_by(Employees.id))

for row in query:
    print(f"{row.id}, {row.FIO}, {row.Avg_salary}, {row.Avg_bonus}, {row.email}")