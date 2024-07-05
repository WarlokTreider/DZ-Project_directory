from datetime import datetime


def calculate_salary():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Функция расчета зарплаты | Дата и время: {current_date}')
