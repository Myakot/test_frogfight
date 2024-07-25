import asyncio
import random

from classes import Assassin, Adventurer, Craftsman, Sniper, Tank
from logger import logger


async def fight(frog1, frog2):

    frog1.modify_params()
    frog2.modify_params()

    frog1_health = frog1.health
    frog2_health = frog2.health

    while frog1_health > 0 and frog2_health > 0:
        frog1_damage = frog1.calculate_damage()
        frog2_armor = frog2.calculate_armor()
        frog1_final_damage = frog1_damage - frog2_armor
        # print('DEBUG', frog1.calculate_damage(), frog2.calculate_armor())
        # Tank armor works, dmg random and armor random works
        frog2_health -= frog1_final_damage

        logger.debug(f"{frog1.__class__.__name__}1 наносит {frog1_damage} урона против {frog2_armor} брони")

        if frog2_health <= 0:
            logger.info(f"{frog1.__class__.__name__}1 победил в этой битве!")
            return 1

        frog2_damage = frog2.calculate_damage()
        frog1_armor = frog1.calculate_armor()
        frog2_final_damage = frog2_damage - frog1_armor
        frog1_health -= frog2_final_damage

        logger.debug(f"{frog2.__class__.__name__}2 наносит {frog2_damage} урона против {frog1_armor} брони")

        if frog1_health <= 0:
            logger.info(f"{frog2.__class__.__name__}2 победил в этой битве!")
            return 2


async def run_fight():
    frog_classes = [Assassin, Adventurer, Craftsman, Sniper, Tank]
    frog1_class = random.choice(frog_classes)
    frog2_class = random.choice(frog_classes)

    frog1 = frog1_class()
    frog2 = frog2_class()

    winner = await fight(frog1, frog2)
    return winner


async def run_battles():
    frog1_wins = 0
    frog2_wins = 0

    tasks = []
    for _ in range(100):
        tasks.append(run_fight())
        tasks.append(run_fight())

    results = await asyncio.gather(*tasks)

    for result in results:
        if result == 1:
            frog1_wins += 1
        else:
            frog2_wins += 1

    print(f"Жаба 1 выиграла {frog1_wins} раз")
    print(f"Жаба 2 выиграла {frog2_wins} раз")


async def main():
    await run_battles()


asyncio.run(main())
