from character import Character
from fight import fight
from hit_dmg import HitEvent


laguna = Character(
    name="Laguna",
    faction="Crane",
    role="Support",
    base_hp=5_051_294,
    base_atk=92_741,
    atk=92_741,
    base_armor=3_432,
    speed=1_460,
    skill_dmg=0,
    block_chance=0,
    crit_rate=0.25,
    crit_dmg=0,
    dmg_reduction=0.05,
    control_resist=0.1,
    hit_chance=0.10,
    mutagen="A",
    armor_break=0,
    true_damage=0,
    control_precision=0.10,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
)

def okami_basic(self, team1: list, team2: list) -> list:
        ennemies = team1 if self in team2 else team2
        target = ennemies[0]
        hits = HitEvent(self, target, self.atk, 1, 0, 0, False, True, "normal", 1)
        return [hits]

def zemus_basic(self, team1: list, team2: list) -> list:
        ennemies = team1 if self in team2 else team2
        target = ennemies[0]
        hits = HitEvent(self, target, self.atk, 1.75, 0, self.true_damage, False, True, "normal", 1)
        return [hits]

okami = Character(
    name="Okami",
    faction="Crane",
    role="Brawler",
    base_hp=4_832_800,
    base_atk=79_194,
    atk=79_194,
    base_armor=2_346,
    speed=1_313,
    skill_dmg=0,
    block_chance=0.0,
    crit_rate=0.55,
    crit_dmg=0.25,
    dmg_reduction=0.05,
    control_resist=0,
    hit_chance=0.26,
    mutagen="S",
    armor_break=0.0,
    true_damage=0.0,
    control_precision=0.0,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
    normal_atk=okami_basic,
)

zemus = Character(
    name="Zemus",
    faction="Cobra",
    role="Finisher",
    base_hp=4_832_800,
    base_atk=97_444,
    atk=97_444,
    base_armor=2_395,
    speed=1_308,
    skill_dmg=0,
    block_chance=0.0,
    crit_rate=0.6,
    crit_dmg=0.45,
    dmg_reduction=0.05,
    control_resist=0,
    hit_chance=0.0,
    mutagen="S",
    armor_break=0.0,
    true_damage=0.0,
    control_precision=0.0,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
    normal_atk=okami_basic,
)

manequin = Character(
    name="Manequin",
    faction="None",
    role="None",
    base_hp=999_999_999,
    base_atk=0,
    atk=0,
    base_armor=0,
    speed=0,
    skill_dmg=0,
    block_chance=0.0,
    crit_rate=0.0,
    crit_dmg=0.0,
    dmg_reduction=0.0,
    control_resist=0,
    hit_chance=0.0,
    mutagen="S",
    armor_break=0.0,
    true_damage=0.0,
    control_precision=0.0,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
)

def skill_bot(self, team1: list, team2: list) -> list:
        ennemies = team1 if self in team2 else team2
        target = ennemies[0]
        hits = HitEvent(self, target, self.atk, 1.75, 0, self.true_damage, False, True, "normal", 1)
        return [hits]

bot1 = Character(
    name="Bot1",
    faction="Mantis",
    role="Mage",
    base_hp=438,
    base_atk=101,
    atk=101,
    base_armor=122,
    speed=231,
    skill_dmg=0,
    block_chance=0.0,
    crit_rate=1.0,
    crit_dmg=0.0,
    dmg_reduction=0.0,
    control_resist=0,
    hit_chance=0.0,
    mutagen="S",
    armor_break=0.0,
    true_damage=0.0,
    control_precision=0.0,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
)



bot2 = Character(
    name="Bot2",
    faction="Mantis",
    role="Finisher",
    base_hp=581,
    base_atk=90,
    atk=90,
    base_armor=104,
    speed=217,
    skill_dmg=0,
    block_chance=0.0,
    crit_rate=1.0,
    crit_dmg=0.0,
    dmg_reduction=0.0,
    control_resist=0,
    hit_chance=0.0,
    mutagen="S",
    armor_break=0.0,
    true_damage=0.0,
    control_precision=0.0,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
    normal_atk=skill_bot
)



print("=" * 50)
print("       ⚔️  Okami  vs  Laguna  ⚔️")
print("=" * 50)

fight(team1=[bot1], team2=[bot2], nb_rounds=1)

print("\n--- État final ---")
print(f"bot1  : {'Vivant' if bot1.is_alive else 'Mort'} — HP : {max(0, int(bot1.hp))}/{bot1.hp_max}")
print(f"bot2  : {'Vivante' if bot2.is_alive else 'Morte'} — HP : {max(0, int(bot2.hp))}/{bot2.hp_max}")

