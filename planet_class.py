class Planet:

    def __init__(self, name: str, planet_type: str, star: str):
        if not all(isinstance(attr, str) for attr in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")

        if not all((name, planet_type, star)):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name: str = name
        self.planet_type: str = planet_type
        self.star: str = star

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

planet_1: Planet = Planet("Earth", "terrestrial", "Sun")
planet_2: Planet = Planet("55 Cancri Af", "hycean", "55 Cancri A")
planet_3: Planet = Planet("Satrun", "misspelled", "no star")

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
