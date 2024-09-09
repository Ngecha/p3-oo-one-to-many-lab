class Pet:
    
    PET_TYPES=["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        
        if pet_type not in Pet.PET_TYPES:
         raise Exception("Pet not on the list")
        
        self.pet_type=pet_type
        self.owner=owner
        self.add_to_All()
        
    def  add_to_All(name):
        if name not in Pet.all:
            Pet.all.append(name)
    
    
class Owner:
    def __init__(self,name):
        self.name=name
        
    
    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
        
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of the Pet class.")
        pet.owner = self   
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)