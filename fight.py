from hit_dmg import resolve_hit

def fight(team1:list, team2:list, nb_rounds:int) -> None:
    """
    Permet de simulter un combat entre 2 équipes.
    Chaque équipe est stockée dans une liste de personnages (un objet de la classe Character).
    Une équipe est composée de 6 personnages, répartis en 2 lignes positions 0 à 2 pour la première ligne, et positions 3 à 5 pour la seconde ligne.
    Le combat se déroule en plusieurs rounds (nb_rounds), et se termine lorsque tous les personnages d'une équipe sont morts ou lorsque le nombre de rounds est atteint.
    À chaque round, les personnages de chaque équipe attaquent chacun leur tour, en se basant sur leur stat de speed (plus la stat de speed est élevée, plus le personnage attaque tôt dans le round).
    Les personnages commencent avec 50 points d'énergie, sauf indication contraire. Lorsqu'un personnage attaque, s'il a plus de 100 points d'énergie, il utilise sa compétence spéciale (skill) et tombe à 0 d'énergie. Sinon, il utilise son attaque de base (normal_atk) et gagne 50 d'énergie.

    """


    for char in team1 + team2:
        char.on_battle_start(team1, team2)
        for weapon in char.weapons:
            weapon.on_battle_start(team1, team2)
        for dragon in char.dragons:
            dragon.on_battle_start(team1, team2)

    for round in range(nb_rounds):
        print(f"Round {round + 1}")
        all_characters = team1 + team2
        all_characters.sort(key=lambda char: char.speed, reverse=True)

        # Boucle pour appliquer les effets de début de round
        for char in all_characters:
            if char.is_alive():
                char.on_round_start(team1, team2)
                for weapon in char.weapons:
                    weapon.on_round_start(team1, team2)
                for dragon in char.dragons:
                    dragon.on_round_start(team1, team2)

        # Boucle pour que chaque personnage attaque
        for char in all_characters:
            if char.is_alive() and char.can_play:
                if char.energy >= 100 and not char.is_silenced:
                    hits = char.skill(team1, team2)
                    for hit in hits:
                        resolve_hit(hit)
                    char.energy = 0
                    char.on_skill()
                    for weapon in char.weapons:
                        weapon.on_skill()
                    for dragon in char.dragons:
                        dragon.on_skill()
                else:
                    hits = char.normal_atk(team1, team2)
                    for hit in hits:
                        resolve_hit(hit)
                    char.energy += 50
                    char.on_normal_atk()
                    for weapon in char.weapons:
                        weapon.on_normal_atk()
                    for dragon in char.dragons:
                        dragon.on_normal_atk()

        # Boucle pour appliquer les effets de fin de round
        for char in all_characters:
            if char.is_alive():
                for dot in char.dots:
                    resolve_hit(dot)
                char.on_round_end(team1, team2)
                for weapon in char.weapons:
                    weapon.on_round_end(team1, team2)
                for dragon in char.dragons:
                    dragon.on_round_end(team1, team2)


        #  Vérification de la fin du combat
        if all(not char.is_alive() for char in team1):
            print("Team 2 wins!")
            return
        elif all(not char.is_alive() for char in team2):
            print("Team 1 wins!")
            return

