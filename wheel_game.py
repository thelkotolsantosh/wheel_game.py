#!/usr/bin/env python3
"""
CLI Wheel Game
Author: Santosh | GitHub: thelkotolsantosh

A terminal-based interactive wheel game demonstrating
game loops, animation, scoring, and user input.
"""

import time
import random
import secrets
import sys

MAX_SPINS = 5
WHEEL_NUMBERS = list(range(1, 11))


def clear():
    sys.stdout.write("\033c")
    sys.stdout.flush()


def pick_number():
    return secrets.choice(WHEEL_NUMBERS)


def draw_wheel(pointer_index):
    clear()
    print("\n🎡 GIANT NUMBER WHEEL 🎡\n")

    for i, num in enumerate(WHEEL_NUMBERS):
        if i == pointer_index:
            print(f"   ➤  {num}")
        else:
            print(f"      {num}")

    print("\nSpinning...\n")


def spin_animation(final_number):
    cycles = random.randint(25, 40)
    idx = 0

    for _ in range(cycles):
        draw_wheel(idx)
        idx = (idx + 1) % len(WHEEL_NUMBERS)
        time.sleep(0.08)

    final_index = WHEEL_NUMBERS.index(final_number)
    draw_wheel(final_index)
    time.sleep(0.5)


def main():
    score = 0
    spins_left = MAX_SPINS

    clear()
    print("🎮 CLI WHEEL GAME 🎮")
    print(f"You have {MAX_SPINS} spins. Numbers range from 1 to 10.")
    input("\nPress ENTER to start...")

    while spins_left > 0:
        clear()
        print(f"Spins left: {spins_left}")
        print(f"Score: {score}")
        input("\nPress ENTER to spin the wheel...")

        result = pick_number()
        spin_animation(result)

        score += result
        spins_left -= 1

        print(f"\nYou landed on: {result}")
        print(f"Total score: {score}")

        if spins_left > 0:
            input("\nPress ENTER for next spin...")

    clear()
    print("🏁 GAME OVER 🏁")
    print(f"Final Score: {score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
