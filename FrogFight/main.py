import asyncio
import random
from classes import Assassin, Adventurer, Craftsman


async def fight(frog1, frog2):
    frog1.modify_params()
    frog2.modify_params()

    frog1_health = frog1.health
    frog2_health = frog2.health

    while frog1_health > 0 and frog2_health > 0:
        frog1_damage = frog1.calculate_damage() - frog2.calculate_armor()
        frog2_health -= frog1_damage

        if frog2_health <= 0:
            return 1

        frog2_damage = frog2.calculate_damage() - frog1.calculate_armor()
        frog1_health -= frog2_damage

        if frog1_health <= 0:
            return 2


async def run_fight():
    frog_classes = [Assassin, Adventurer, Craftsman]
    frog1_class = random.choice(frog_classes)
    frog2_class = random.choice(frog_classes)

    frog1 = frog1_class()
    frog2 = frog2_class()

    winner = await fight(frog1, frog2)
    return winner


async def run_battles():
    frog1_wins = 0
    frog2_wins = 0

    for _ in range(100):
        winner = await run_fight()
        if winner == 1:
            frog1_wins += 1
        else:
            frog2_wins += 1

    print(f"Жаба 1 выиграла {frog1_wins} раз")
    print(f"Жаба 2 выиграла {frog2_wins} раз")


async def main():
    await asyncio.gather(run_battles(), run_battles())


asyncio.run(main())
