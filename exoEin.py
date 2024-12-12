nbPersonne = int(input("How many people need a ride?"))

placeTaxi = int(input("How many people fit in one taxi?"))

nbTaxi = nbPersonne // placeTaxi

if ( (nbPersonne % placeTaxi) != 0):
    nbTaxi += 1


print("le nombre de taxi necessaire est de :",nbTaxi)
