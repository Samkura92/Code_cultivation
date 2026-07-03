class fleur:
    def __init__(self, height, age):
        self.age = age
        self.height = height


def ft_garden_data():
    Rose = fleur(25, 30)
    Sunflower = fleur(80, 45)
    Cactus = fleur(15, 120)
    print("=== Garden Plant Registry ===")
    print(f'Rose: {Rose.height}cm, {Rose.age} days old')
    print(f'Sunflower: {Sunflower.height}cm, {Sunflower.age} days old')
    print(f'Cactus: {Cactus.height}cm, {Cactus.age} days old')


if __name__ == "__main__":
    ft_garden_data()
