from character import Character
from fight import fight


kael = Character(
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
    crit_dmg=0.3,
    dmg_reduction=0.0,
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

lyra = Character(
    name="Okami",
    faction="Crane",
    role="Brawler",
    base_hp=9500,
    base_atk=3200,
    atk=3200,
    base_armor=700,
    speed=110,
    skill_dmg=0.55,
    block_chance=0.08,
    crit_rate=0.20,
    crit_dmg=0.45,
    dmg_reduction=0.10,
    control_resist=0.15,
    hit_chance=0.05,
    mutagen="S",
    armor_break=200.0,
    true_damage=0.0,
    control_precision=0.20,
    stealth=0.0,
    weapons=[],
    dragons=[],
    position=0,
)

print("=" * 50)
print("       ⚔️  KAEL  vs  LYRA  ⚔️")
print("=" * 50)

fight(team1=[kael], team2=[lyra], nb_rounds=20)

print("\n--- État final ---")
print(f"Kael  : {'Vivant' if kael.is_alive else 'Mort'} — HP : {max(0, int(kael.hp))}/{kael.hp_max}")
print(f"Lyra  : {'Vivante' if lyra.is_alive else 'Morte'} — HP : {max(0, int(lyra.hp))}/{lyra.hp_max}")