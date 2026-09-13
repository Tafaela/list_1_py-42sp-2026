class Plant:
    def age(self):
        self.plant_age = self.plant_age + 1

    def grow(self):
        self.height = self.height + 0.8

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    initial_height = rose.height
    rose.plant_age = 30

    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")
