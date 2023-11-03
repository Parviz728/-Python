import random
from types import FunctionType
from typing import List, Tuple
friends = [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'}, 
           {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}
]

# select = query(select)
def select(*field_name: Tuple[str]):
    def inner():
        for i in range(len(friends)):
            change = {}
            for field in field_name:
                change[field] = friends[i][field]
            friends[i] = change
    return inner

def field_filter(field_name: str, collection: list):
    def inner():
        for i in range(len(friends)):
            if i < len(collection):
                friends[i][field_name] = collection[i]
            else:
                friends[i][field_name] = collection[-1]
    return inner

def query(collection: List[dict], select: FunctionType, *field_filter):
    select()
    for func in field_filter:
        func()
 
res_of_select = select("name", "gender", "sport") # -> function
res_of_filed_filter1 = field_filter("sport", ["Баскетбол", "Волейбол"]) # -> function
res_of_field_filter2 = field_filter("gender", ["Мужской"]) # -> function

query(friends, 
      res_of_select, 
      res_of_filed_filter1,
      res_of_field_filter2,
      )
print(friends)
        
        
        
        
        