import requests
from datetime import datetime


def fetch_github_events():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Функция получения событий GitHub | Дата и время: {current_date}')
    response = requests.get('https://api.github.com/events')
    if response.status_code == 200:
        events = response.json()
        print(f'Последние события на Github:')
        for event in events[:5]:
            print(f"-{event['type']} от {event['actor']['login']} на {event['repo']['name']}")

    else:
        print('Не удалось получить данные с GitHub')
