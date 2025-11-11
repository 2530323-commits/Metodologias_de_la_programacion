"""
Slicing a list
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("list original : ", players)

print("Slice de lista orginal",players[0:3])
print("slice de lista original", players[1:4])
print("slice de lista original", players[:4])
print("slice de lista original", players[2:])       
print("slice de lista original", players[-3:])


"""
Slicing en un for
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print ("Aqui se presentan los primeros 3 jugadores del equipo")
for player in players[0,3]:
    print(player.title())

"""
Copiando una lista
"""
my_foods = ['pizza', 'tacos', "flautas", "gorditas"]
#my_foods_copy = my_foods # Error : esta no es la manera de copiar
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my foods_3 = list(my_foods)
