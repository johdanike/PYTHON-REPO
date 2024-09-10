for multiples_column in range(1, 13):
    for multiples_row in range(1, 13):
        print(f"{multiples_row:>2}  * {multiples_column:>2} = {multiples_column * multiples_row:<4}", end= "    ")
    print()