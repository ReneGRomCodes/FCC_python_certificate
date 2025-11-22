class GameCharacter:

    def __init__(self, name: str):
        self._name: str = name
        self._health: int = 100
        self._mana: int = 50
        self._level: int = 1

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, new_mana: int) -> None:
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self) -> int:
        return self._level

    def level_up(self) -> None:
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")


# Usage example.
hero: GameCharacter = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)                    # Displays the character's stats

hero.health -= 30              # Decreases health by 30
hero.mana -= 10                # Decreases mana by 10
print(hero)                    # Displays the updated stats

hero.level_up()                # Levels up the character
print(hero)                    # Displays the stats after leveling up
