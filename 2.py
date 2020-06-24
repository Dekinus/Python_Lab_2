import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import random

seaborn.set_context('poster') # общий стиль графика (шрифты и т.д.)
#print(plt.style.available) # вывод доступных стилей графика
plt.style.use('fivethirtyeight')  # Стиль графика
plt.rcParams['figure.figsize'] = (25, 15)  # Размер изображения (*100 пикселей)

def graph(company):
    df = pd.read_csv(company+'.csv', sep=',') # считывание csv файла
    df = df.iloc[::-1]  # обратный порядок
    #print(df) # вывод считанных данных
    df['Date'].plot(x="Date", y="Price", label=company, color='C'+str(random.randint(0,50))) # построение графика: по оси x -- дата, по оси y -- цена, Название -- Компания, Цвет -- CN палитра (где N определяется случайным образом
    plt.legend(loc='upper left')    # Легенда в левом верхнем углу
    #plt.show() # построение графика в отдельном окне
    path = 'Graphs' + '/' + company + '.png'    # путь сохранения изображений
    plt.savefig(path)   #   сохранение
    plt.close('all') # Закрытие файла

graph('Apple')
graph('Amazon')
graph('Facebook')
graph('Google')
graph('Netflix')
