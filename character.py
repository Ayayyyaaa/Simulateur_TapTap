class Character:
    def __init__(self, name: str, faction: str, role: str, base_hp: int,
                 base_atk: int, atk: int, base_armor: int, speed: int, skill_dmg: float, 
                 block_chance: float, crit_rate: float, crit_dmg: float, dmg_reduction: float, control_resist: float, 
                 hit_chance: float, mutagen: str, armor_break: float, true_damage: float, control_precision: float, stealth: float,
                 weapons: list, dragons: list, position: int, on_ally_die=None, on_ennemi_die=None, on_dmg_taken=None, 
                 on_hit=None, normal_atk=None, skill=None, on_battle_start=None, on_round_start=None,
                 on_round_end=None, on_killing_blow=None):
        """
        Paramètres :
            - name (str) : Nom du combattant
            - faction (str) : Faction du combattant (parmi Crane, Howler, Mantis, Kodiak, Griffin, Cobra). Permet d'appliquer les avantages de faction (+30% de dégâts et +15% de hit_chance) et de maîtrise.
            - role (str) : Rôle du combattant (parmi Mage, Finisher, Tank, Support, Brawler). Permet d'appliquer les bonus de maîtrise ou certains buffs.
            - base_hp (int) : Hp de base du combattant. Sert de valeur de base pour tous les multiplicateurs hp%.
            - hp_max (int) : Hp max du combattant. Valeur des hp après l'application de tous les buffs hp%.
            - hp (int) : Hp actuels du combattant. Ils ne peuvent pas dépasser les hp_max, et s'ils tombent à 0, le combattant meurt.
            - base_atk (int) : Attaque de base du combattant. Sert de valeur de base pour tous les multiplicateurs atk%.
            - atk (int) : Attaque actuelle du combattant. Valeur de l'attaque après l'application de tous les buffs atk%. Permet de déterminer le montant de dégâts infligés par le combattant.
            - base_armor (int) : Armure de base du combattant. Sert de valeur de base pour tous les multiplicateurs armor%.
            - armor (int) : Armure actuelle du combattant. Valeur de l'armure après l'application de tous les buffs armor%. Permet de réduire les dégâts subis. Plus l'armure est élevée, moins le combattant subira de dégâts.
            - speed (int) : Vitesse du combattant. Permet de déterminer l'ordre d'attaque dans un combat. Plus la vitesse est élevée, plus le combattant attaque en 1er.
            - skill_dmg (float) : Multiplicateur (>= 0) de dégâts pour le skill. Il permet d'augmenter les dégâts d'un skill avec la formule [dgts_skill * (1 + skill_dmg)]
            - block_chance (float) : Chance de bloquer (0 < block_chance < 1) un coup (diminuer les dégâts par 2).
            - crit_rate (float) : Chance de lancer un coup critique (0 < crit_rate < 1). Par défaut, elle est de 0.15.
            - crit_dmg (float) : Multiplicateur de dégâts (0 < crit_dmg < 10) appliqué lors d'un coup critique. Par défaut, elle est de 0.3. Un coup critique permet de multiplier les dégâts de l'attaque par la formule [dgts_atk * (1 + crit_dmg)]
            - dmg_reduction (float) : Multiplicateur appliqué pour réduire les dégâts (0 < dmg_reduction < 1). Réduit les dégâts avec la formule : [dégâts * (1-dmg_reduction)]
            - control_resist (float) : Chance (0 < control_resist < 1) de résister à un effet de paralysie : [multi_cc * (1 + attacker.control_precision - target.control_resist)]
            - hit_chance (float) : Chance (0 < hit_chance < 1) d'infliger une attaque malgré les chances de parade. Les chances de parer le coup sont donc de [target.block_chance - attacker.hit_chance]
            - mutagen (str) : Valeur parmi S, A, B, C, D. Permet de définir les bonus fournis par les mutagens sur le combattant.
            - armor_break (str) : _
            - true_damage (float) : Portion de l'attaque qui ignore l'armure (mais pas la réduction de dégâts). Multiplicateur entre 0 et 1.
            - control_preicison (float) : Chance (0 < control_resist < 1) d'infliger un effet de paralysie malgré le control_resist : [multi_cc * (1 + attacker.control_precision - target.control_resist)]
            - stealth (float) : Permet de ne pas etre ciblé par les attaques ennemies.
            - weapons (list) : liste de 3 armes équipées sur le combattant.
            - dragons (list) : liste de 2 dragons équipés sur le combattant.
            - position (int) : Entier compris entre 0 et 5. Répresente la position dans l'équipe : 0 à 2, 1re ligne, 3 à 5, 2nd ligne. 0 est devant 3, 1 devant 4 et 2 devant 5.
            - energy (int) : Energie du perso. Avec 100, permet de lancer un skill. Au dela de 100, la moitié excédant 100 est convertie en skill_dmg (ex 140 energie = + 20% skill_dmg sur le skill)
            - is_alive (bool) : Détermine si le combattant est en vie ou non
            - can_play (bool) : Détermine si le combattant peut attaquer (s'il est stun, freeze, pétrifié, sleep)
            - is_silenced (bool) : Détermine si le combattant peut utiliser son skill
            - effect (list) : liste de tous les effets (classe buff ou debuff) qui s'appliquent actuellement sur le personnage (avec leur durée)
            - immune (list) : liste des debuffs auxquels sont immunisés
            - basic_dmg_taken (float) : multiplicateur compris entre 0 et 1 qui augmente les dégâts subis par une attaque normale
            - skill_dmg_taken (float) : multiplicateur compris entre 0 et 1 qui augmente les dégâts subis par un skill
            - heal_effect (float) : Multiplicateur compris entre 0 et 2. Détermine le montant de soins reçus. 

            - on_ally_die (function) : hook qui s'applique quand un allié meurt (pour déclencher un comportement spécifique au combattant). Est appelé dans resolve_hit.
            - on_ennemi_die (function) : hook qui s'applique quand un ennemi meurt (pour déclencher un comportement spécifique au combattant). Est appelé dans resolve_hit.
            - on_dmg_taken (function) : hook qui s'applique quand un le combattant subit des dégâts (pour déclencher un comportement spécifique au combattant). Est appelé dans resolve_hit.
            - on_hit (function) : hook qui s'applique quand un le combattant inflige des dégâts (pour déclencher un comportement spécifique au combattant). Est appelé dans resolve_hit.
            - on_killing_blow (function) : hook qui s'applique quand un le combattant inflige un coup fatal (pour déclencher un comportement spécifique au combattant). Est appelé dans resolve_hit.

            - normal_atk (function) : attaque normale du combattant. Elle détermine quel(s) ennemi(s) cibler, les multiplicateurs de base des hits, créer un objet hit et peut appliquer des effets propres au perso. est appelé dans fight.
            - skill (function) : skill du combattant. Elle détermine quel(s) ennemi(s) cibler, les multiplicateurs de base des hits, créer un objet hit et peut appliquer des effets propres au perso. est appelé dans fight.

            - on_battle_start (function) : hook qui s'applique lorsque le combat débute. Permet d'appliquer divers buffs/debuffs propres au combattant. Est appelé dans fight.
            - on_round_start (function) : hook qui s'applique lors du début d'un round. Permet d'appliquer divers buffs/debuffs propres au combattant. Est appelé dans fight.
            - on_round_end (function) : hook qui s'applique lors de la fin d'un round. Permet d'appliquer divers buffs/debuffs propres au combattant. Est appelé dans fight.
        """
        # Infos générales
        self.name = name
        self.faction = faction
        self.role = role
        self.position = position
        self.mutagen = mutagen
 
        # Stats de base (référence des buffs %)
        self.base_hp = base_hp
        self.base_atk = base_atk
        self.base_armor = base_armor
 
        # Stats du combat (actuelles)
        self.hp_max = base_hp
        self.hp = base_hp
        self.atk = base_atk
        self.armor = base_armor
 
        # Vitesse et énergie
        self.speed = speed
        self.energy = 50
 
        # Stats d'attaque
        self.skill_dmg = skill_dmg
        self.crit_rate = crit_rate      # def = 0.15
        self.crit_dmg = crit_dmg        # def = 0.3
        self.true_damage = true_damage
        self.armor_break = armor_break
        self.hit_chance = hit_chance
        self.control_precision = control_precision
 
        # Stats de défense
        self.block_chance = block_chance
        self.dmg_reduction = dmg_reduction
        self.control_resist = control_resist
        self.stealth = stealth
 
        # Dégâts subis supplémentaires
        self.basic_dmg_taken = 0.0
        self.skill_dmg_taken = 0.0
 
        # Soin
        self.heal_effect = 1.0
 
        # Équipement
        self.weapons = weapons if weapons is not None else []
        self.dragons = dragons if dragons is not None else []
 
        # Variables d'état pdn le combat
        self.is_alive = True
        self.can_play = True
        self.is_silenced = False
        self.effects = []
        self.immune = []
        self.dots = []

        # Compétences et hooks
        self._normal_atk = normal_atk if normal_atk else self.normal_atk
        self._skill = skill if skill else self.skill
        self._on_battle_start = on_battle_start if on_battle_start else self.on_battle_start
        self._on_round_start = on_round_start if on_round_start else self.on_round_start
        self._on_round_end = on_round_end if on_round_end else self.on_round_end
        self._on_ally_die = on_ally_die if on_ally_die else self.on_ally_die
        self._on_ennemi_die = on_ennemi_die if on_ennemi_die else self.on_ennemi_die
        self._on_dmg_taken = on_dmg_taken if on_dmg_taken else self.on_dmg_taken
        self._on_hit = on_hit if on_hit else self.on_hit
        self._on_killing_blow = on_killing_blow if on_killing_blow else self.on_killing_blow


    def normal_atk(self, team1: list, team2: list) -> list:
        return []
 
    def skill(self, team1: list, team2: list) -> list:
        return []
 
    def on_battle_start(self, team1: list, team2: list):
        print("On battle start")

    def on_round_start(self, team1: list, team2: list):
        pass
 
    def on_round_end(self, team1: list, team2: list):
        pass
 
    def on_ally_die(self, team1: list, team2: list):
        pass
 
    def on_ennemi_die(self, team1: list, team2: list):
        pass
 
    def on_dmg_taken(self, event, dmg: float, team1: list, team2: list):
        pass
 
    def on_hit(self, event, dmg: float, team1: list, team2: list):
        pass
 
    def on_killing_blow(self):
        pass
 