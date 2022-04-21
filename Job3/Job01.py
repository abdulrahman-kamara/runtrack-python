#Récursivité

#write all the positive even numbers smaller or equal to 8 

# def Evennum(num):
#     print(num)
#     if num % 2 != 0:
#         print('please enter an even number ')
#     elif num == 2: # first we tackle the base case which is 2 and check if the num value is equal to 2 which is the last number
#         return num
#     else: # If not we call our else and subtract it from our num 
#         return Evennum(num -2)
# Evennum(12) # and finnally we call our recursive function that take the value we want to loop through

def Fibonacci(idx):
    if idx <= 1: # we tackle our base case
        return idx 
    else: # we
        return Fibonacci(idx - 1) + Fibonacci(idx - 2)
print(Fibonacci(8))