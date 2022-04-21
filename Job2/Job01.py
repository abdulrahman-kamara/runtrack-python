from ast import Return

# #Using inheritance

# class User():
#     def log(self):
#         print(self)


# # using polymorphism

# class Teacher(User):
#     def log(self):
#         print('I am a Teacher')


# class Customer(User): #declearing the class and inheriting the parent class user
#     def __init__(self, name, membership_type): # giving the class a constructor or initializer or method that takes a parameters
#         self.name = name
#         self.membership_type = membership_type # attribute of the classes

#         # making name a property 
#     @property # a decorator and this is our we say this is a property
#     def name(self): # this just a way to say don't touch this if you are not within the class because this is private.
#         return self._name # To access this data we have to invoke another method 
    
#     @name.setter
#     def name(self, name): 
#         self._name = name

#     # we also have deleter property

#     @name.deleter
#     def name(self):
#         del self._name

#     def __str__(self):
#         print('this will invoke when we try to convert a customer to string') #this will invoke when we try to convert a customer to string
#         return self.name + ' ' + self.membership_type


#     def print_all_customers(customers):
#         for customer in customers:
#             print(customer)
        
#     def __eq__(self, other): # the __eq__ method is used to compare two customers
#         if self.name == other.name and self.membership_type == other.membership_type:
#            return True
        
#         return False

#     __hash__ = None # hash block you to use your customers inside of your data structures

#     __repr__ = __str__ # __repr__ we overide  representation by asign it to __str__

# # The three main principe of OOP are 
# # 1. encapsulation: this allow you to communicate with data through the Getter methods and setter methods using a property
# # 2. Inheritance: this allow  automatically to have certain attribute for object because they are defined in a base class
# # 3. Polymophism: this add allow us to treate sub classes(method) as the same thing if the have the same base class. But the sub class can also do there stuff separatelly
    

# users = [Customer('Kunta', 'Gold'), Customer('Borris', 'Bronze'), Teacher()] # instances of the class that takes aguement

# # del customers[0]._name
# # print(customers[0].name)
# # customers[2].log()

# for user in users:
#     user.log()



class SePerson():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def setName(self, value):
        self.__nom = value

    def getName(self):
        return self.__nom
    


A1 = SePerson('kunta', 'kamara')
A2 = SePerson('ahcane', 'Alex')

print(A1.nom)
print(A2.prenom)


class Livre:
    def __init__(self, titre, Auteur):
        self.titre = titre
        self.Auteur = Auteur

    def printTitre(self):
        print(self.titre)





class Auteur(SePerson):
    def __init__(self, nom, prenom):
        SePerson.__init__(self, nom, prenom)
        self.listerOeuvre = []




    def listerOeuvre(self):
        print('the books writting by the auteur')
        if(len(self.listerOeuvre) == 0):
            print('the is a book')

    def ecrireUnLivre(self, titre):
        input('the aeuter of the book: ')
        self.titre = titre



C1 = Auteur('borris', 'Alex')
C1.ecrireUnLivre('book man')


    
        




    





        


