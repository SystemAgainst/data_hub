import os

import gspread
from django.conf import settings
from django.core.cache import cache
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet_stats(sheet_url):
    """
    Принимает ссылку на Google Таблицу.
    Возвращает словарь со статистикой или None, если ошибка.
    """

    # 1. Проверяем кэш (чтобы не дергать Google каждую секунду)
    # Ключ уникален для каждой ссылки
    cache_key = f"sheet_stats_{sheet_url}"
    cached_data = cache.get(cache_key)

    if cached_data:
        # Если данные есть в памяти - возвращаем их сразу!
        print("Data from cache")
        return cached_data

    print("Fetching from Google API...")  # Для отладки в логах

    try:
        # 2. Путь к ключу (мы его положили в корень backend/)
        # settings.BASE_DIR указывает на папку, где лежит manage.py
        creds_path = settings.BASE_DIR / "credentials.json"

        # Проверка на всякий случай
        if not os.path.exists(creds_path):
            print(f"CRITICAL: Файл {creds_path} не найден!")
            return None

        # 3. Подключаемся к Google
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(str(creds_path), scope)
        client = gspread.authorize(creds)

        # 4. Открываем таблицу по ссылке
        sheet = client.open_by_url(sheet_url).sheet1  # Берем первый лист

        # 5. ЧИТАЕМ ДАННЫЕ (Ваш скриншот)
        # Нам нужен прямоугольник данных:
        # От ячейки K1 (заголовки участников) до L7 (итоговые дни)
        # Метод get вернет список списков (массив массивов)
        data = sheet.get("K1:M7")

        # data будет выглядеть примерно так:
        # [
        #   ['Грайр', 'Павел', 'Зоро'],         <- row 0 (headers)
        #   ['3 395 192,00', '0,00', '0,00'],   <- row 1 (values)
        #   ...
        #   ['Потрачено всего', 'Всего дней'],  <- row 6 (labels)
        #   ['3 595 192,00', '83']              <- row 7 (totals)
        # ]

        if not data:
            return None

        # Разбираем участников (берем 0-ю строку как имена, 1-ю как суммы)
        participants_headers = data[0]
        participants_values = data[1]

        participants_list = []
        for name, money in zip(participants_headers, participants_values):
            if name and name.strip():  # Пропускаем пустые колонки
                participants_list.append({"name": name, "amount": money})

        # Разбираем Итого (последняя строка данных)
        # Внимание: индекс -1 берет последнюю строку, сколько бы их ни было
        totals_row = data[-1]

        # Простая защита от выхода за границы массива
        total_spent = totals_row[0] if len(totals_row) > 0 else "0"
        total_days = totals_row[1] if len(totals_row) > 1 else "0"

        result = {
            "total_spent": total_spent,
            "total_days": total_days,
            "participants": participants_list,
        }

        # 6. Сохраняем в кэш на 10 минут (600 секунд)
        cache.set(cache_key, result, 600)

        return result

    except Exception as e:
        print(f"Google Sheet Error: {e}")
        return None
