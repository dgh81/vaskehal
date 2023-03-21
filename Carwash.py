from PIL import Image
import customtkinter

class Car:
    def __init__(self, owner, licence_plate):
        self.owner = owner
        self.licence_plate = licence_plate

class CarCategori1(Car):
    def __init__(self, owner, licence_plate):
        super().__init__(owner, licence_plate)
        self.time = 20
        self.image = customtkinter.CTkImage(Image.open("./images/car.png"), size=(40,40))

    def getImage(self):
        return self.image

class CarCategori2(Car):
    def __init__(self, owner, licence_plate):
        super().__init__(owner, licence_plate)
        self.time = 30
        self.image = customtkinter.CTkImage(Image.open("./images/van.png"), size=(60,40))

    def getImage(self):
        return self.image

class CarCategori3(Car):
    def __init__(self, owner, licence_plate):
        super().__init__(owner, licence_plate)
        self.time = 45
        self.image = customtkinter.CTkImage(Image.open("./images/truck.png"), size=(60,40))

    def getImage(self):
        return self.image

class Carwash():
    def __init__(self):
        self.car_list = []

    def add_car(self, bilkategori):
        self.car_list.append(bilkategori)

    def remove_car(self, licence_plate):
        for car in self.car_list:
            if car.licence_plate == licence_plate:
                self.car_list.remove(car)   

    def remove_first_car(self):
        self.car_list = self.car_list[1:]

    def get_total_cue_time(self):
        cue_time_sum = 0
        for car in self.car_list[1:]:
            cue_time_sum += car.time
        return cue_time_sum

    def get_car_time(self, licence_plate):
        for car in self.car_list:
            if car.licence_plate == licence_plate:
                return car.time
        
    def get_car_cue_time(self, licence_plate):
        cue_time = 0
        try:
            for car in self.car_list[:[carIndex for carIndex, car in enumerate(self.car_list) if car.licence_plate == licence_plate][0]]:
                cue_time += car.time
            return cue_time
        except:
            print('Please enter a valid vehicle licence plate.')
            return None    

# Test af funktioner. Exkluderet fra GUI.
def main():
    
    k1 = CarCategori1('Daniel', 'AJ60500')

    print(k1.time)

    MinVaskehal = Carwash()

    MinVaskehal.add_car(k1)

    for car in MinVaskehal.car_list:
        print(car.time)

    k2 = CarCategori2('Thomas', 'DN34522')

    MinVaskehal.add_car(k2)

    print("Vaskehallen indeholder biler med disse tider: ")
    for car in MinVaskehal.car_list:
        print(car.time)

    MinVaskehal.add_car(CarCategori3('Susanne', 'KP98631'))

    print("Vaskehallen indeholder biler med disse tider: ")
    for car in MinVaskehal.car_list:
        print(car.time)

    MinVaskehal.remove_car(k1)

    print("Vaskehallen indeholder biler med disse tider: ")
    for car in MinVaskehal.car_list:
        print(car.time)

    MinVaskehal.remove_first_car()

    print("Vaskehallen indeholder biler med disse tider: ")
    for car in MinVaskehal.car_list:
        print(car.time)

    print('get_total_koetid()',MinVaskehal.get_total_cue_time())

    MinVaskehal.get_car_time('KP98631')

    k3 = CarCategori2("Sofus", "KL09876")
    MinVaskehal.add_car(k3)

    MinVaskehal.get_car_time('KL09876')

if __name__ == '__main__':
    main()