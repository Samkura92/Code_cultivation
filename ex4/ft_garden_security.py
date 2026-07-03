class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        if new_height < 0:
            print("Rose: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f'Height updated: {new_height}cm')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0:
            print("Rose: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f'Age updated: {new_age} days')


def ft_garden_securtity():
    plants = Plant("Rose", 20, 20)
    plants.get_height()
    plants.get_age()
    print("=== Garden Security System ===")
    print(f"Plant created: {plants.name}: {plants.get_height()}cm,"
          f"{plants.get_age()} days old")
    print("")
    plants.set_height(15)
    plants.set_age(10)
    print("")
    print(f"Current state: {plants.name}: "
          f"{plants.get_height()}cm, {plants.get_age()} days olf")


if __name__ == "__main__":
    ft_garden_securtity()
