class Plant():
    class Stats:
        def __init__(self):
            self.grow_c = 0
            self.age_c = 0
            self.show_c = 0

        def affiche(self):
            print(f"Stats: {self.grow_c} grow, "
                  f" {self.age_c} age, {self.show_c} show")

    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages
        self._stats = self.__class__.Stats()

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.ages} days old")
        self._stats.show_c += 1

    def grow(self):
        self.height = self.height + 40
        self._stats.grow_c += 1

    def age(self):
        self.ages = self.ages + 40
        self._stats.age_c += 1

    @staticmethod
    def comparaison_age(age):
        if age > 365:
            print(f"Is {age} more than a year ? -> True")
        else:
            print(f"Is {age} more than a year ? -> False")

    @classmethod
    def unknow_p(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True
        return f"{self.name} is blooming beautifully!"

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_c = 0

        def affiche(self):
            super().affiche()
            print(f"{self.shade_c} shade")

    def __init__(self, name, height, ages, trunk_dia):
        super().__init__(name, height, ages)
        self.trunk_dia = trunk_dia

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}"
              f"cm long and {self.trunk_dia}cm wide.")
        self._stats.shade_c = + 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_dia}cm")


class Seed(Flower):
    def __init__(self, name, height, ages, color, seed_c):
        super().__init__(name, height, ages, color)
        self.seed_c = seed_c

    def seed_compte(self):
        self.seed_c = self.seed_c + 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seed_c if self.bloomed else 0}")


def affiche_stat(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.affiche()


def ft_garden_analytics():
    lotus = Flower("Lotus", 15.0, 10, "White")
    sakura = Tree("Sakura", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow", 0)
    unknow = Plant.unknow_p()
    print("=== Garden statistics ===")
    print("=== Check years_old")
    Plant.comparaison_age(30)
    Plant.comparaison_age(400)
    print("")
    print("=== Flower")
    lotus.show()
    affiche_stat(lotus)
    print("[asking the rose for to grow and bloom]")
    lotus.grow()
    lotus.bloom()
    lotus.show()
    affiche_stat(lotus)
    print("")
    print("=== Tree")
    sakura.show()
    affiche_stat(sakura)
    print("[asking the sakura to produce shade]")
    sakura.produce_shade()
    affiche_stat(sakura)
    print("")
    print("=== Seed")
    seed.show()
    print("[make sunflower grow, age, and bloom]")
    seed.age()
    seed.grow()
    seed.bloom()
    seed.seed_compte()
    seed.show()
    affiche_stat(seed)
    print("")
    print("=== Anonymous")
    unknow.show()
    print(f"[statistics for {unknow.name}]")
    unknow._stats.affiche()


if __name__ == "__main__":
    ft_garden_analytics()
