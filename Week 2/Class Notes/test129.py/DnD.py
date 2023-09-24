# Player v Player

class Player:
    '''
    Attributes:
    - hp: health point. Overall health points for the character.
    - atk: attack/damage amount
    -defence: amount subtracted from the attack points
    
    Method:
    - attack(): launches an attack against another player, resulting in damage taken.
    
    
    '''
def __init__(self, hp=50, atk=6, defence=4):
    self.hp = hp
    self.atk = atk
    self.defence = defence

def attack(self, target):
    damage = self.atk - target.defence
    if damage > 0:
        target.hp -= damage


