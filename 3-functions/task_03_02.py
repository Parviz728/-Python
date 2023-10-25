import random
from types import FunctionType
friends = [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'}, 
           {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}
]

# отсюда будем брать данные
db = {"name": ["Парвиз", "Ваня", "Женя", "Лёша", "Настя"],
      "sport": ["Баскетбол", "Волейбол", "Футбол", "Теннис", "Хоккей"],
      "gender": ["Мужик", "НеМужик"],
      "email": ["parviz@korus.ru", "Ivan@korus.ru", "zhenyok@korus.ru", "lekha@korus.ru", "nastya@korus.ru"]}

count = len(friends)
ans = [{} for i in range(count)] # создаем столько пустых словарей, сколько значений в списке friends

def select(*field_name):
    for d in ans:
        for i in field_name:
            d[i] = None

# select("name", "sport", "gender")
# print(ans)

def field_filter(field_name: str, collection: list):
    for i in range(len(ans)):
        ans[i][field_name] = collection[i]

# field_filter("sport", ["Баскетбол", "Волейбол"])
# print(ans)

def query(collection: list, select: FunctionType, *field_filter: FunctionType) -> list:
    select(*random.choices(list(db.keys()), k=random.randint(1, len(db))))
    print(f"ans = {ans}")
    for f in field_filter:
        x = random.choice(list(db.keys()))
        print(f"x = {x}, db[x] = {db[x]}")
        f(x, db[x])
    
    return ans

print(query(friends, select, field_filter))
        



