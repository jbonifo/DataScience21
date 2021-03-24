class ListKeeper :
     
# Initializer : initializes the instance with a dictionnay containing already example
    def __init__(self):
        self.Keeper = {'example': [1,2,3,4,5]}
        
# This method prints on the scren all keys of the dictionnary
    def show(self):
        for key in self.Keeper:
            print(key)
            
# Adds a list with a name as key to the dictionnary
    def add(self, name, list):
        self.Keeper[name]=list
        print(self.Keeper)

# Deletes an item from the dictionnary with the name of the key
    def delete(self, name):
        self.Keeper.pop(name)
        print(self.Keeper)
        
# Prints on the screen the list of the key selected        
    def sort(self, name):
        print(self.Keeper[name])

# Appends a new list to a key in the dictionnary
    def append(self, name, list):
        self.Keeper[name].extend(list)
        print(self.Keeper[name])
    