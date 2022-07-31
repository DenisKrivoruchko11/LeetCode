def get_money(coins: Dict[int, int], value: int) -> None:
    selected = {}
    for nominal in sorted(coins.keys(), reverse=True):
        count = min(value // nominal, coins[nominal])
        if count > 0:
            selected[nominal] = count
            value -= count * nominal
    if value == 0:
        for nominal in selected:
            coins[nominal] -= selected[nominal]
    else:
        print('Error.')