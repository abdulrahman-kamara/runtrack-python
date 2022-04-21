# Créez un programme qui demande 5 fois à l’utilisateur de renseigner un nombre entier.
# Stockez ces nombres entiers dans une liste puis triez-les par ordre croissant avant de
# les afficher, dans l’ordre, dans le terminal.

li = []
ask = 5
while len(li) < ask:
    p = input('the numbers are : ')
    li.append(int(p))
    li.sort()
    print(li)


   

