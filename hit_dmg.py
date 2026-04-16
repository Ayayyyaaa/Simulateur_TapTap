from random import random

class HitEvent:
    def __init__(self, attacker:'Character', target:'Character', multiplier: float = 1.0, skill_dmg: float = 0.0, true_dmg: float = 0.0, ign_armor: bool = False, can_crit: bool = True, hit_type: str = "normal", duration: int = 1):
        self.attacker = attacker
        self.target = target
        self.multiplier = multiplier
        self.skill_dmg = skill_dmg
        self.true_dmg = true_dmg
        self.ignore_armor = ign_armor
        self.can_crit = can_crit
        self.hit_type = hit_type
        self.duration = duration

    def get_type(self):
        return self.hit_type

def armor_reduction(armor: float, attacker_armor_pen: float = 750) -> float:
    effective_armor = max(0, armor - attacker_armor_pen)
    return effective_armor / (effective_armor + 3450)

def resolve_hit(event: HitEvent, team1: list, team2: list) -> float:
    """
    Couche défensive : armure, réduction, parade, crit, etc.
    Renvoie les dégâts réellement subis.
    """
    target = event.target
    attacker = event.attacker

    allies = team1 if attacker in team1 else team2
    enemies = team2 if attacker in team1 else team1

    dmg = event.base_dmg * event.multiplier
    dmg *= (1 + event.skill_dmg)

    # Modification des dégâts par les armes
    for w in attacker.weapons:
        dmg = w.modify_dmg_dealt(dmg, event.get_type(), target, attacker)
    # Modification des dégâts par les dragons
    for d in attacker.dragons:
        dmg = d.modify_dmg_dealt(dmg, event.get_type(), target, attacker)

    # Calcul du crit
    if event.can_crit and random() < attacker.crit_rate:
        dmg *= attacker.crit_dmg

    # True damage
    true_part = min(event.true_dmg, dmg) 
    physical_part = dmg - true_part


    # Armure
    armor = 0 if event.ignores_armor else target.armor
    armor_factor = 1 - armor_reduction(armor)
    physical_part *= armor_factor


    # Parade
    if random() < (target.parry_chance - attacker.hit_chance):
        physical *= 0.5
        true_part *= 0.5

    # Total
    total = physical + true_part

    # Réduction de dégâts
    final = max(0, total * (1-target.dmg_reduction))

    # Inflige les dégâts et hooks
    target.hp -= final
    attacker.on_hit(event, final, team1, team2)
    target.on_receive_hit(event, final, team1, team2)

    if target.hp <= 0:
        target.is_alive = False
        attacker.on_killing_blow()
        for weapon in attacker.weapons:
            weapon.on_killing_blow()
        for dragon in attacker.dragons:
            dragon.on_killing_blow()
        
        for a in allies:
            a.on_ennemi_die()
            for weapon in a.weapons:
                weapon.on_ennemi_die()
            for dragon in a.dragons:
                dragon.on_ennemi_die()

        for e in enemies:
            e.on_ennemi_die()
            for weapon in e.weapons:
                weapon.on_ennemi_die()
            for dragon in e.dragons:
                dragon.on_ennemi_die()

    return final