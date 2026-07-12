class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def show(self) -> str:
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
        return plant


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_dia: float):
        super().__init__(name, height, age)
        self.trunk_dia = trunk_dia

    def produce_shade(self) -> str:
        return f"Tree {self.name} now produces a shade of {
            self.height} cm long and {self.trunk_dia}cm wide."

    def show(self) -> str:
        plant = super().show()
        print("=== Tree")
        print(f"{plant}")
        print(f"Trunk diameter: {self.trunk_dia}cm")
        print(f"[aksing the {self.name} to produce shade]")
        print(f"{self.produce_shade()}")
        print("")
        return plant


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutri: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutri = nutri

    def ages(self) -> None:
        self.nutri = self.nutri + 20

    def grow(self) -> None:
        self.height = self.height + self.nutri
        self.age = self.age + self.nutri

    def show(self) -> str:
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
        return plant


def ft_plant_types() -> None:
    rose = Flower("Rose", 20.0, 35, "Pink")
    sakura = Tree("Sakura", 200.0, 360, 10.0)
    cerise = Vegetable("Cerise", 2.0, 11, "June", 0)
    print("=== Garden Plant Types ===")
    for plant in [rose, sakura, cerise]:
        plant.show()


if __name__ == "__main__":
    ft_plant_types()
