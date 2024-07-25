"""
Модуль, содержащий основной код приложения.

Этот модуль содержит основной код приложения,
который запускает асинхронные бои двух жаб со случайно выбранными классами.
"""
import asyncio
import random

from classes import Assassin, Adventurer, Craftsman, Sniper, Tank
from logger import logger
from config import FIGHTS


async def fight(toad1, toad2):
    """
    Асинхронная функция для проведения раундов боя между двумя жабами.

    Логирует:
        - информацию о нанесении урона и изменении здоровья жаб.
        - информацию о победителе боя.

    Процесс:
    - Вызывает метод `modify_params` для обеих жаб, чтобы изменить их параметры.
    - Запускает цикл, который продолжается до тех пор, пока у одной из жаб здоровье не упадёт ниже нуля.
    - Вычисляет урон, наносимый первой жабой, и вычитает броню второй жабы.
    - Обновляет здоровье второй жабы и записывает информацию о битве в лог.
    - Повторяет шаги 2-4 для второй жабы асинхронно.
    """

    toad1.modify_params()
    toad2.modify_params()

    toad1_health = toad1.health
    toad2_health = toad2.health

    while toad1_health > 0 and toad2_health > 0:
        toad1_damage = toad1.calculate_damage()
        toad2_armor = toad2.calculate_armor()
        toad1_final_damage = toad1_damage - toad2_armor
        toad2_health -= toad1_final_damage

        logger.debug(f"{toad1.__class__.__name__}1 наносит {toad1_damage} урона против {toad2_armor} брони.\n"
                     f"Здоровье {toad2.__class__.__name__}2: {toad2_health}")

        if toad2_health <= 0:
            logger.info(f"{toad1.__class__.__name__}1 победил в этой битве!")
            return 1

        toad2_damage = toad2.calculate_damage()
        toad1_armor = toad1.calculate_armor()
        toad2_final_damage = toad2_damage - toad1_armor
        toad1_health -= toad2_final_damage

        logger.debug(f"{toad2.__class__.__name__}2 наносит {toad2_damage} урона против {toad1_armor} брони.\n"
                     f"Здоровье {toad1.__class__.__name__}1: {toad1_health}\n")

        if toad1_health <= 0:
            logger.info(f"{toad2.__class__.__name__}2 победил в этой битве!")
            return 2


async def run_fight():
    """
    Асинхронная функция для запуска боевых между двумя жабами.

    Процесс:
        - Выбирает случайные классы жаб.
        - Создает объекты классов жаб.
        - Запускает функцию `fight` для проведения боя.
        - Возвращает номер победившего класса (1 или 2).
    """
    toad_classes = [Assassin, Adventurer, Craftsman, Sniper, Tank]
    toad1_class = random.choice(toad_classes)
    toad2_class = random.choice(toad_classes)

    toad1 = toad1_class()
    toad2 = toad2_class()

    winner = await fight(toad1, toad2)
    return winner


async def run_battles():
    """
    Асинхронная функция для запуска всех боевых между жабами.

    Процесс:
        - Создает список задач для выполнения функции `run_fight` определенное количество раз.
        - Использует `asyncio.gather` для одновременного выполнения всех задач.
        - Обрабатывает результаты битв и подсчитывает количество побед для каждого класса жабы.
    """
    toad1_wins = 0
    toad2_wins = 0

    tasks = []
    for _ in range(FIGHTS):
        tasks.append(run_fight())
        tasks.append(run_fight())

    results = await asyncio.gather(*tasks)

    for result in results:
        if result == 1:
            toad1_wins += 1
        else:
            toad2_wins += 1

    print(f"Жаба 1 выиграла {toad1_wins} раз")
    print(f"Жаба 2 выиграла {toad2_wins} раз")


async def main():
    await run_battles()


asyncio.run(main())
