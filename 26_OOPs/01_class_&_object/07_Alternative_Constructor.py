



class Professor:
    def __init__(self,name,age,id):
        self.name = name
        self.id=id
        self.age = age

    @classmethod
    def from_getDetails(cls,string):
        name,id,age =string.split(",") 
        return cls(name,id,age)   
        


details = "Ravindra singh,123422,22"
prof = Professor.from_getDetails(details)
print(prof.name,int(prof.id),int(prof.age))        
       