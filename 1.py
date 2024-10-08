class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} движется со скоростью {self.speed}")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернулась {direction}")

class townCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class sportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class workCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class policeCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

town_car = townCar(80, 'синий', 'BMW')
sport_car = sportCar(250, 'красный', 'Ferrari')
work_car = workCar(70, 'белый', 'Toyota')
police_car = policeCar(160, 'черный', 'Lada')

town_car.go()
sport_car.go()
work_car.go()
police_car.go()

town_car.stop()
sport_car.stop()
work_car.stop()
police_car.stop()

town_car.turn('налево')
sport_car.turn('направо')