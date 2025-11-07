# Jonathan Sonnek
# November 6 2025
# Program # 2: Car Class

# Create Car Class
class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = 0
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed
# Create Function to add objects to the class & use them
def main():
    car1 = Car(2019, "Ford", 0)
    while car1.get_speed() < 25:
        car1.accelerate()
        print("Speed:", car1.get_speed())
    while car1.get_speed() > 0:
        car1.brake()
        print("Speed:", car1.get_speed())
main()