from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from application.requester import fetch_github_events


def main():
    current_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Запуск программы <Бухгалтерия> | Дата и время: {current_data}')
    calculate_salary()
    get_employees()
    fetch_github_events()

if __name__ == "__main__":
    main()