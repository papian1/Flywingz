#!/usr/bin/env python3
"""
Tebak-Tebakan sederhana (CLI)

Jalankan tanpa argumen untuk mode interaktif.
Gunakan `--auto` untuk menjalankan self-test otomatis (non-interaktif).
"""
import argparse
import random
import sys


def play_interactive():
    print('=== Tebak-Tebakan ===')
    print('Saya memilih angka antara 1 dan 100. Tebaklah!')
    target = random.randint(1, 100)
    attempts = 0
    while True:
        attempts += 1
        try:
            s = input(f'Percobaan #{attempts}, masukkan tebakan: ')
        except (EOFError, KeyboardInterrupt):
            print('\nKeluar. Sampai jumpa!')
            return
        s = s.strip()
        if not s:
            print('Masukkan angka antara 1 dan 100.')
            continue
        if not s.isdigit():
            print('Tolong masukkan angka bulat.')
            continue
        guess = int(s)
        if guess < 1 or guess > 100:
            print('Angka harus di antara 1 dan 100.')
            continue
        if guess < target:
            print('Terlalu rendah.')
        elif guess > target:
            print('Terlalu tinggi.')
        else:
            print(f'Benar! Anda menebak dalam {attempts} percobaan.')
            break


def auto_test():
    """Run a quick non-interactive self-test: deterministic seed and simulated guesses."""
    random.seed(0)
    target = random.randint(1, 100)
    low, high = 1, 100
    attempts = 0
    while True:
        attempts += 1
        guess = (low + high) // 2
        if guess < target:
            low = guess + 1
        elif guess > target:
            high = guess - 1
        else:
            print(f'AUTO-TEST: target={target}, found={guess}, attempts={attempts}')
            return 0
        if attempts > 200:
            print('AUTO-TEST: failed (too many attempts)')
            return 2


def main(argv=None):
    parser = argparse.ArgumentParser(description='Tebak-Tebakan sederhana (CLI)')
    parser.add_argument('--auto', action='store_true', help='jalankan self-test otomatis (non-interaktif)')
    args = parser.parse_args(argv)

    if args.auto:
        return auto_test()
    else:
        play_interactive()
        return 0


if __name__ == '__main__':
    sys.exit(main())
