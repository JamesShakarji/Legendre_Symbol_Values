import numpy
import math
import csv

import csv


def compute_legendre_symbol_table():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113]
    table = []
    for p in prime_numbers:
        row = []
        for a in range(1, 31):
            if a % p == 0:
                row.append(0)
            else:
                legendre_symbol = (a ** ((p - 1) // 2)) % p
                if legendre_symbol == 1:
                    row.append(1)
                else:
                    row.append(-1)
        table.append(row)

    with open('legendre_symbols.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['p'] + [str(a) for a in range(1, 31)])
        for p, row in zip(prime_numbers, table):
            writer.writerow([p] + row)


compute_legendre_symbol_table()
