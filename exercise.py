class Cars:
    def __init__(self,Model,Year_of_Manufacture,Type,Colour):
        self.Model= Model
        self.Year_of_Manufacture= Year_of_Manufacture
        self.Type= Type
        self.Colour= Colour

    def display(self):
            print(f"My dream car is {self.Model} manufactured in {self.Year_of_Manufacture} being a {self.Type} in {self.Colour}")

        #object
My_dream_car= Cars('Suzuki','2007','Alto','Green')
My_dream_car.display()
My_dream_car= Cars('Jaguar','2020','XF','Grey')
My_dream_car.display()
My_dream_car= Cars('Range Rover','2020','Sport','Black')
My_dream_car.display()
