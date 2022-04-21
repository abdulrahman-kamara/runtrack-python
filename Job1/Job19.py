# Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple

def rectangle(width, height):
    for line in range(width):
        if line < width:
            print('|', end = '')
            for i in range(height):
                if line == 0 or line == width - 1:
                    if i < height - 1:
                        print('-', end ="")
                    elif i == height -1:
                         print('|')
                else:
                    if i < height - 1:
                        print(' ', end ="")
                    elif i == height -1:
                        print('|')
    
rectangle(3, 10)
    



 


   


  
