inventory_player1 = ["sword", "wood", "axe", "armor", "letter"]
inventory_player2 = []

def item_list():
    """Esta función sirve para asignar un número a cada ítem del inventario 1
    con qué identificarlo. A su vez, por cada iteración que realice
    el for loop, se añadirá un número a la variable number. Es decir,
    "wood es igual a 0", y en la siguiente iteración, el próximo ítem será 1,
    y así. Una vez hecho eso, imprime "Si desea regalar...", y la opción al usuario
    de seleccionar el número asignado al objeto que se desea regalar, si
    es que quisiera."""

    number = 0
    for item in inventory_player1:
        print (item + " is number " + str (number))
        number = number + 1
    choice = str (input ("Si desea regalar algún objeto, selecciónelo. "))

    gift_item (choice)


def gift_item(item):
    """ Esta función sirve para, si en la opción anterior se seleccionó
    un número, agregar al inventario 2 dicho objeto, y eliminarlo del inventario 1. Luego,
    imprime cómo quedaron ambos inventarios. Si no se selecciona nada, da lugar a la siguiente función."""
    if item is not "":
        print ("Se ha regalado " + inventory_player1 [int(item)])
        print ("Se ha eliminado " + inventory_player1 [int(item)] + " de su inventario.")
        inventory_player2.append (inventory_player1 [int(item)])
        print ("se ha añadido " + inventory_player1 [int(item)] + " al player 2")
        del inventory_player1 [int(item)]

        print (inventory_player1)
        print (inventory_player2)

    else:

        add_all_items ()

def add_all_items ():
    """Esta función sirve para que, si no se selecciona ningún objeto en la función anterior,
    se dé la opción al usuario de regalar todos los objetos del inventario 1 con "E". Si
    esa es la decisión, mientras en el inventario 1 haya algún objeto, se agregará al 2 el elemento 0. Por
    cada iteración, se eliminará el elemento 0 del inventario 1, pasando el ítem siguiente a ser 0, y así
    sucesivamente, hasta vaciar la lista y no haya nada más que itinerar. Luego, se imprimirá
    que se ha vaciado la lista 1 y se han agregado todos los elementos a la lista 2, y se imprimirán
    ambas listas para ver cómo quedaron. Por otro lado, si la opción no fue "E", se imprimirá "eres egoísta".  """

    choice_2 = input ("si desea regalar todos los objetos, presione E")

    if choice_2 is "E":
        counter = 0
        while len (inventory_player1) > 0:

            inventory_player2.append (inventory_player1[0])
            del inventory_player1 [0]

            counter = counter + 1

        print ("Se han eliminado todos los objetos de su inventario")
        print ("se han añadido todos los objetos al player 2")

        print (inventory_player1)
        print (inventory_player2)

    else:
        print ("You are really selfish")

item_list ()
