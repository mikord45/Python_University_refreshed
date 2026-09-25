class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

    def promote(self, new_position, new_salary):
        self.position = new_position
        self.salary = new_salary
        return f"{self.name} has been promoted to {new_position} with a salary of {new_salary}"

    def calculate_bonus(self, bonus_percentage):
        bonus_amount = self.salary * (bonus_percentage / 100)
        return f"{self.name} received a bonus of {bonus_amount}"


employee1 = Employee(1, "John Doe", "Manager", 50000)
print(employee1.display_info())
print(employee1.promote("Senior Manager", 60000))
print(employee1.calculate_bonus(20))
print("=====")

class Monster:
    def __init__(self, name, health, damage, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = level

    def attack(self):
        return f"{self.name} attacks for {self.damage} damage!"

    def receive_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} has {self.health} health remaining."

    def level_up(self):
        self.level += 1
        self.health += 20
        self.damage += 5
        return f"{self.name} leveled up to level {self.level}!"


monster1 = Monster("Goblin", 100, 20, 5)
print(monster1.attack())
print(monster1.receive_damage(30))
print(monster1.level_up())
print("=====")


class Refrigerator:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return f"Added {item} to the refrigerator."

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"Removed {item} from the refrigerator."
        else:
            return f"{item} is not in the refrigerator."

    def list_items(self):
        return f"Items in the refrigerator: {', '.join(self.items)}"


fridge = Refrigerator("Samsung", 500)
print(fridge.add_item("Milk"))
print(fridge.add_item("Eggs"))
print(fridge.list_items())
print(fridge.remove_item("Eggs"))
print(fridge.list_items())