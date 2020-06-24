import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import matplotlib.pyplot as plt

def is_car(title):
    s = "цена"
    if (str(title).rfind(s) != -1): # если найдена подстрока "цена"
        return title    # возвращаем всю строку

def get_car(title):
    k = str(title).find(',') # позиция первого вхождения запятой
    s = title[0:k]  # выделение подстроки с названием
    return s    # возвращение этой подстроки

def get_price(title):
    k = title.rfind('цена') # позиция вхождения подстроки "цена"
    l = title.rfind('руб') - 1 # позиция вхождения подстроки "руб"
    s1 = title[k + 5:l] # выделение подстроки с ценой с учётом пробелов
    return s1   # возвращение этой подстроки

def get_year(title):
    k = title.find(',') # позиция первого вхождения запятой
    s = title[k:len(title)] # выделение всей подстроки после запятой
    s1 = s[2:6]  # выделение подстроки длинной 4 символа (год)
    return s1 # возвращение этой подстроки

def get_city(title):
    k = title.rfind('Автомобили в') # позиция вхождения подстроки "Автомобили в"
    s = title[k + 11:len(title)] # выделение подстроки со сдвигом на 11 до конца (город)
    return s # возвращение этой подстроки

df = pd.DataFrame({'марка': [], 'цена': [], 'год выпуска': [], 'город': []}) # создание таблицы pandas
pages = 3  # количество анализируемых страниц
base_url = 'https://www.avito.ru/mordoviya/avtomobili?cd=1'
for i in range(pages): # цикл по просматриваемым страницам
    url = base_url.format(str(i)) # форматирование ссылки
    resp = req.get(url) # передача ссылки
    soup = BeautifulSoup(resp.text, "html.parser") # парсинг
    links = soup.findAll('a') #заголовки
    #print(links) # тест


    for link in links:
         title = link.get('title') # все элементы
        # print(title) # вывод элементов
         if is_car(title): # если найдена подстрока "цена"
             df1 = pd.DataFrame( # добавляем в датафрейм
                 {'марка': [get_car(title)], 'цена': [get_price(title)], 'год выпуска': [get_year(title)],
                  'город': [get_city(title)]}) # распределение по столбцам
             df = df.append(df1, ignore_index=True) # добавить строку df1 в df

print(df) # вывод датафрейма
df.to_csv("avito_cars.csv")  # создаем csv  из Dataframe
df_by_city = df.groupby('город')  # сортировка по городам
print(df_by_city.get_group("в Саранске"))  # Машины в Саранске
df_by_model = df.groupby('марка')  # сортировка по моделям
print(df_by_model.get_group("LADA Granta"))  # Lada granta



