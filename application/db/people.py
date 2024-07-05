from datetime import datetime


def get_employees():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Функция получения списка сотрудников | Дата и время: {current_date}')