from fighter import *
from exchange import *
from round import *

def main():
    raff = Fighter("raff")
    amine = Fighter("amine")
    round1 = Round(raff, amine)
    print(f"Round 1 winner is {round1.winner.name}")
    print(f"Amine health: {amine.health}")
    print(f"Raff health: {raff.health}")

    round2 = Round(raff, amine)
    print(f"Round 2 winner is {round2.winner.name}")
    print(f"Amine health: {amine.health}")
    print(f"Raff health: {raff.health}")

    round3 = Round(raff, amine)
    print(f"Round 3 winner is {round3.winner.name}")
    print(f"Amine health: {amine.health}")
    print(f"Raff health: {raff.health}")

main()