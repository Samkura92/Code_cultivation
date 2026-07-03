class plant:
    def __init__(self, height, age):
        self.age = age
        self.height = height

    def evolution(self):
        self.height = self.height + 0.8
        self.age = self.age + 1


def ft_plant_growth():
    Rose = plant(25, 30)
    print("=== Garden Plant Growth ===")
    print(f'Rose : {round(Rose.height)}cm, {Rose.age} days old')
    for i in range(1, 8):
        Rose.evolution()
        print("=== Day", i, "===")
        print(f'Rose : {round(Rose.height, 2)}cm, {Rose.age} days old')
    height_final = round(Rose.height, 2)
    res = round(height_final - 25, 2)
    print(f'Growth this week: {res}cm')


if __name__ == "__main__":
    ft_plant_growth()
