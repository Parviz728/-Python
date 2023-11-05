from peewee import Model, PostgresqlDatabase, CharField, DateField, FloatField, IntegerField, ForeignKeyField
from decouple import config

PASSWORD = config('PASSWORD')

db = PostgresqlDatabase(database="postgres", user="postgres", password=PASSWORD)

class BaseModel(Model):
    class Meta:
        database = db
    
class Employees(BaseModel):
    surname = CharField()
    name = CharField()
    fatherName = CharField()
    
class Emails(BaseModel):
    empID = ForeignKeyField(Employees)
    email = CharField()
    
class Salary(BaseModel):
    empID = ForeignKeyField(Employees)
    date = DateField()
    salaryType = CharField()
    amount = FloatField()
    
db.create_tables([Employees, Emails, Salary])