

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show_info(self):
        print(f"Name:- {self.name}")     
        print(f"Species:- {self.species}")     
        

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed= breed 


    def show_info(self):
        super().show_info()
        print(f'Breed:- {self.breed}')


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Golden Retriever")
        self.color = color 

    def show_info(self):
        super().show_info()
        print(f"Color:- {self.color}") 

gr = GoldenRetriever("tommy","black")
gr.show_info()

print(GoldenRetriever.mro())
               