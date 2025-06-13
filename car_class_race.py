import random

class Car:
    def __init__(self, color, location):
        self.color = color
        self.fuel_consumption = random.uniform(0.08, 0.12)
        self.max_speed = random.randint(150, 210)
        self.tank_capacity = 50
        self.fuel = self.tank_capacity
        self.location = location
        self.state = "driving"
        self.time = 0
        self.refuel_time = random.randint(3, 7)
        self.current_station = None

    def drive(self, time_step):
        if self.state != "driving":
            return
        max_dist = self.max_speed * time_step
        fuel_dist = self.fuel / self.fuel_consumption
        dist = min(max_dist, fuel_dist)
        self.location += dist
        self.fuel -= dist * self.fuel_consumption
        self.time += time_step
        if self.fuel <= 0:
            self.state = "needs_refuel"

    def refuel(self, time_step):
        if self.state != "refueling":
            return
        self.refuel_time -= time_step
        self.time += time_step
        if self.refuel_time <= 0:
            self.fuel = self.tank_capacity
            self.state = "driving"
            self.refuel_time = random.randint(3,7)
            if self.current_station:
                self.current_station.remove_car(self)
                self.current_station = None

    def update(self, time_step, stations):
        if self.state == "driving":
            self.drive(time_step)
            if self.state == "needs_refuel":
                nearest_station = min(stations, key=lambda s: abs(s.location - self.location))
                if nearest_station.can_accept_car():
                    nearest_station.add_car(self)
                    self.current_station = nearest_station
                    self.state = "refueling"
                else:
                    self.state = "waiting"
        elif self.state == "refueling":
            self.refuel(time_step)
        elif self.state == "waiting":
            if self.current_station and self.current_station.can_accept_car():
                self.state = "refueling"
                self.current_station.add_car(self)

    def finished(self, finish_line):
        return self.location >= finish_line

class FuelStation:
    def __init__(self, location):
        self.location = location
        self.capacity = 4
        self.cars_in_station = []

    def can_accept_car(self):
        return len(self.cars_in_station) < self.capacity

    def add_car(self, car):
        if self.can_accept_car():
            self.cars_in_station.append(car)

    def remove_car(self, car):
        if car in self.cars_in_station:
            self.cars_in_station.remove(car)

def create_cars():
    colors = ["قرمز", "آبی", "سبز"]
    cars = []
    last_location = 0
    for color in colors:
        location = last_location + random.randint(500, 700)
        car = Car(color, location)
        cars.append(car)
        last_location = location
    return cars

def create_stations():
    stations = []
    for _ in range(3):
        location = random.randint(0, 10000)
        stations.append(FuelStation(location))
    return stations

def run_race():
    distance = 10000
    cars = create_cars()
    stations = create_stations()

    finished_cars = []
    time_step = 1

    while len(finished_cars) < len(cars):
        for car in cars:
            if car.finished(distance):
                if car not in finished_cars:
                    finished_cars.append(car)
                continue

            car.update(time_step, stations)

    winner = min(finished_cars, key=lambda c: c.time)
    print(f"برنده: ماشین {winner.color} با زمان {round(winner.time, 2)}")

if __name__ == "__main__":
    run_race()