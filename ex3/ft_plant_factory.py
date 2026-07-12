class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'Created: {self.name}: {self.height}cm, {self.age} days old')


def ft_plant_factory() -> None:
    name = ["Sakura", "Rose", "Lotus", "Anemone", "Lilas"]
    height = [200.0, 25.0, 80.0, 30.0, 27.0]
    age = [365, 30, 45, 32, 35]
    print("=== Plant Factory Output ===")
    for i in range(5):
        Plant(name[i], height[i], age[i]).show()


if __name__ == "__main__":
    ft_plant_factory()
