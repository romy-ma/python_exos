total_amount = float(input("Montant total de l'achat : "))
number_of_items = int(input("Nombre d'articles : "))
day_of_week = input("Jour de la semaine : ").strip().capitalize()

discount = 0

if day_of_week in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]:
    discount += 10
elif day_of_week in ["Samedi", "Dimanche"]:
    discount += 20

if number_of_items > 5:
    discount += 5

final_price = total_amount * (1 - discount / 100)

print(f"Prix total apres remise : {final_price:.1f} dinars")
