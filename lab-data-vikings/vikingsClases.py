
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

        
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
# War


class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        try:
            text = self.saxonArmy[0].receiveDamage(self.vikingArmy[0].attack())
            if self.saxonArmy[0].health < 0:
               del self.saxonArmy[0] 
        except:
            pass
        
        return text
    
    def saxonAttack(self):
        try:
            text = self.vikingArmy[0].receiveDamage(self.saxonArmy[0].attack())
            if self.vikingArmy[0].health < 0:
               del self.vikingArmy[0] 
        except:
            pass
        
        return text    
    
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."

    
