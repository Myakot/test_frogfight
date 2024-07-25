import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('toad_fights.log', mode='w')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

"""
Модуль, содержащий настройки логгера для приложения.

Этот модуль настраивает логгер для записи информации о процессе боев между жабами.
Логгер настроен на вывод сообщений с уровнями DEBUG, INFO.
Вывод сообщений форматируется с помощью формата '%(asctime)s - %(levelname)s - %(message)s'.

Файл лога сохраняется в 'toad_fights.log'.

Дополнительная информация:
    - https://docs.python.org/3/library/logging.html
"""
