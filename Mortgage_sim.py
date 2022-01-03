from decimal import Decimal

def mortgage_sim(principal, interest_rate, years=30, payments_per_year=52):
    p = principal
    n = years * payments_per_year
    r = interest_rate / 100 / payments_per_year

    left = p
    paid = 0
    num = 1

    while True:
        c = (r * p) / (1 - (1+r)**(-n))

        paid += c
        left -= c
        print(f"Payment number: {num} Paid: {paid:.2f} Remaining: {left:.2f} {c:.2f}")
        if num >= n:
            break
        num += 1

mortgage_sim(472_000, interest_rate=2.29)




