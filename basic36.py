class CharacterAlreadyExistException(Exception):
    pass

class AllCharacters:
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターは既に存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:
    def __init__(self, name, hp, offence, defence):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence
    
    def attack(self, other, critical=1):
        if self.hp <= 0:
            print(f'キャラクター{self.name}はすでに死んでします')
            return
        damage = self.offence - other.defence
        damage = 1 if damage <= 0 else damage
        other.hp -= damage * critical
        if other.hp <= 0:
            AllCharacters.character_delete(other.name)

    def critical_hit(self, other):
        self.attack(other, 2)
        
    

    
character_a = Character('A', 10, 5, 3)
character_b = Character('B', 8, 6, 2)
print(character_b.hp)
character_a.attack(character_b)
print(character_b.hp)
character_a.critical_hit(character_b)
print(character_b.hp)
character_b.attack(character_a)
character_c = Character('A', 15, 4, 3)