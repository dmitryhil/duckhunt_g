import datetime
import os
from dateutil.relativedelta import relativedelta
import csv

def read_data(filename, product_name):
    # Удаление файла old_data.csv, если он существует
    try:
        os.remove("data.txt")
    except OSError:
        pass
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        # Получение цены продукта и даты
        for row in reader:
            if row[0] == product_name:
                date_ = datetime.datetime.strptime(row[1], "%d/%m/%Y").date()
                price_ = float(row[2])
                return (date_, price_)

def analyze_price_changes(start_price, end_price):
    # Расчет процентного изменения цены
    percentage_change = ((end_price - start_price) / start_price) * 100
    return round(percentage_change, 2)

# Пример использования функций
filename = "data.csv"
product_name = "Product Name"

start_date, start_price = read_data(filename, product_name)

# Вручну введіть кінцеву ціну
end_price = float(input("Введіть кінцеву ціну: "))

change = analyze_price_changes(start_price, end_price)
print(f"Зміна ціни за період: {change}%")
