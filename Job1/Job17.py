#summer = 0
#for i in range(1, 101, 3):
    #summer = summer + i
    #print(summer,i)
#print("Fizz", summer)

#summer = 0
#for i in range(1, 101, 5):
    #summer = summer + i
    #print(summer,i)
#print("buzz", summer)

# (1+2+3+4+5+6....+m)1000
# s=0
# i=0
# while s<=1000:
#     i=i+1
#     s=s+i
#     print(s,i)
# print(i)

# Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les multiples de
# trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
# les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".

for i in range(1, 100):
    i = i + 1
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
    
         
        
        

        














