class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"

    def show(self):
        plant = super().show()
        print("=== Flower")
        print(f"{plant}")
        print(f"Color: {self.color}")
        print("Rose has not bloomed yes")
        print(f"[asking the {self.name} to bloom]")
        print(f"{plant}")
        print(f"Color: {self.color}")
        print(f"{self.bloom()}")
        print("")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_dia):
        super().__init__(name, height, age)
        self.trunk_dia = trunk_dia

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}"
              f"cm long and {self.trunk_dia}cm wide.")

    def show(self):
        plant = super().show()
        print("=== Tree")
        print(f"{plant}")
        print(f"Trunk diameter: {self.trunk_dia}cm")
        print(f"[aksing the {self.name} to produce shade]")
        print(f"{self.produce_shade()}")
        print("")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutri):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutri = nutri

    def ages(self):
        self.nutri = self.nutri + 20

    def grow(self):
        self.height = self.height + self.nutri
        self.age = self.age + self.nutri

    def show(self):
        plant = super().show()
        print("=== Vegetable")
        print(f"{plant}")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrional value: {self.nutri}")
        self.ages()
        self.grow()
        plant_g = super().show()
        print(f"[make {self.name} grow and age {self.nutri} for days]")
        print(f"{plant_g}")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrional value: {self.nutri}")
        print("")


def ft_plant_types():
    rose = Flower("Rose", 20.0, 35, "Pink")
    sakura = Tree("Sakura", 200.0, 360, 10.0)
    cerise = Vegetable("Cerise", 2.0, 11, "June", 0)
    print("=== Garden Plant Types ===")
    for plant in [rose, sakura, cerise]:
        plant.show()


if __name__ == "__main__":
    ft_plant_types()
