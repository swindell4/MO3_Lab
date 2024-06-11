#This program stores instance variables of vehicle types with a class until a user is finished, then prints the collected 
#data with pprint.  
class Vehicle: 
   def __init__(self, _vehicle): 
      self.type = _vehicle 
class Automobile(Vehicle): 
   def __init__(self, _vehicle, _year, _make, _model, _doors, _roof): 
      super().__init__(_vehicle) 
      self.year = _year 
      self.make = _make 
      self.model = _model 
      self.doors = _doors 
      self.roof = _roof 
   def storeTheData(self): 
      global counter, data 
      data.append(f"Car {counter}") 
      counter += 1 
      data.append(f"Year: {self.year}") 
      data.append(f"Make: {self.make}") 
      data.append(f"Model: {self.model}") 
      data.append(f"Door Options: {self.doors}") 
      data.append(f"Roof Options: {self.roof}") 
      return data 
correct = str("") 
data = [] 
Done = str("No") 
counter = int(1) 
while correct != "Yes": 
   vehicle = str(input(f"Please enter a vehicle type. \n")) 
   correct = str(input(f"You entered {vehicle}. Is this information correct? \"Yes\" or \"No\"? \n")) 
   while correct != "Yes" and correct != "No": 
      correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
while Done != "Yes": 
   correct = "No" 
   while correct != "Yes": 
      year = str(input(f"Please enter a car year. \n")) 
      correct = str(input(f"You entered {year}. Is this information correct? \"Yes\" or \"No\"? \n")) 
      while correct != "Yes" and correct != "No": 
         correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   correct = "No" 
   while correct != "Yes": 
      make = str(input(f"Please enter a car make. \n")) 
      correct = str(input(f"You entered {make}. Is this information correct? \"Yes\" or \"No\"? \n")) 
      while correct != "Yes" and correct != "No": 
         correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   correct = "No" 
   while correct != "Yes": 
      model = str(input(f"Please enter a car model. \n")) 
      correct = str(input(f"You entered {model}. Is this information correct? \"Yes\" or \"No\"? \n")) 
      while correct != "Yes" and correct != "No": 
         correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   correct = "No" 
   while correct != "Yes": 
      doors = str(input(f"Please enter a car door count. Your options are \"Two\" or \"Four\". Case sensitive. \n")) 
      while doors != "Two" and doors != "Four": 
         doors = str(input(f"{doors} is an invalid input. Your options were \"Two\" or \"Four\". Case sensitive. \n")) 
      correct = str(input(f"You entered {doors}. Is this information correct? \"Yes\" or \"No\"? \n")) 
      while correct != "Yes" and correct != "No": 
         correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   correct = "No" 
   while correct != "Yes": 
      roof = str(input(f"Please enter a car roof option. Your options are \"Solid Roof\" or \"Sun Roof\". Case sensitive. \n")) 
      while roof != "Solid Roof" and roof != "Sun Roof": 
         roof = str(input(f"{roof} is an invalid input. Your options were \"Solid Roof\" or \"Sun Roof\". Case sensitive. \n")) 
      correct = str(input(f"You entered {roof}. Is this information correct? \"Yes\" or \"No\"? \n")) 
      while correct != "Yes" and correct != "No": 
         correct = str(input(f"{correct} was an invalid response. Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   auto = Automobile(vehicle, year, make, model, doors, roof) 
   data = auto.storeTheData() 
   Done = str(input(f"Are you done entering car information? Your options are \"Yes\" or \"No\". Case sensitive. \n")) 
   while Done != "Yes" and Done != "No": 
      Done = str(input(f"{Done} was an invalid response. Are you done entering information. \"Yes\" or \"No\"? Case sensitive. \n")) 
counter = 0 
while counter < len(data): 
   print(data[counter]) 
   counter += 1 