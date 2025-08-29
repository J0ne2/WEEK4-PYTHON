# Parent class: Superhero
class Superhero:
    def _init_(self, name, superpower, health):
        self.name = name
        self.superpower = superpower
        self.__health = health  # private attribute (encapsulation)

    def show_info(self):
        print(f"Hero: {self.name}, Power: {self.superpower}, Health: {self.__health}")

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0
        print(f"{self.name} took {amount} damage! Health now: {self.__health}")

    def heal(self, amount):
        self.__health += amount
        if self.__health > 100:
            self.__health = 100
        print(f"{self.name} healed by {amount}! Health now: {self.__health}")


# Child class: FlyingSuperhero inherits from Superhero
class FlyingSuperhero(Superhero):
    def _init_(self, name, superpower, health, flight_speed):
        super()._init_(name, superpower, health)
        self.flight_speed = flight_speed

    # Overriding show_info method (polymorphism)
    def show_info(self):
        print(f"Hero: {self.name}, Power: {self.superpower}, Health: {self.Superhero_health}, Flight Speed: {self.flight_speed} km/h")


# Testing
hero1 = Superhero("IronShield", "Super Strength", 90)
hero1.show_info()
hero1.take_damage(20)
hero1.heal(15)

hero2 = FlyingSuperhero("SkyWing", "Flight & Laser Eyes", 80, 250)
hero2.show_info()
hero2.take_damage(30)
hero2.heal(20)