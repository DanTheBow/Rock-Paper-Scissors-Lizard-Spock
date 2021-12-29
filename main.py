from random import choice

print("Willkommen bei Schere, Stein, Papier, Echse, Spock!")
print("Das Ziel des Spiels ist es als erster 2 Punkte zu erreichen.")
print("Zu den Regeln:")
print("Schere schneidet Papier, Papier bedeckt Stein, Stein zerquetscht Echse, Echse vergiftet Spock,")
print("Spock zertrümmert Schere, Schere köpft Echse, Echse frisst Papier, Papier widerlegt Spock,")
print("Spock verdampft Stein. Und wie gewöhnlich – Stein schleift Schere.")
print()


def action_to_text(action):
    if action == "sc":
        return "Schere gewählt"
    elif action == "st":
        return "Stein gewählt"
    elif action == "pa":
        return "Papier gewählt"
    elif action == "ec":
        return "Echse gewählt"
    elif action == "sp":
        return "Spock gewählt"
    else:
        return "dich wohl vertippt. Versuche es erneut!"


def score():
    print("Gegner: " + str(computer_points) + " | " + "Du: " + str(user_points))
    print()


user_points = 0
computer_points = 0

while True:
    if user_points == 2:
        print("Du hast das Spiel gewonnen!")
        user_points, computer_points = 0, 0
        run = input("Möchtest du noch einmal spielen (j/n)? ")
        print()
        if run == "n":
            break
    elif computer_points == 2:
        print("Der Gegner hat das Spiel gewonnen!")
        user_points, computer_points = 0, 0
        run = input("Möchtest du noch einmal spielen (j/n)? ")
        print()
        if run == "n":
            break
    else:
        user_action = input("Wähle Schere(sc), Stein(st), Papier(pa), Echse(ec), Spock(sp): ")
        actions = ["sc", "st", "pa", "ec", "sp"]
        computer_action = choice(actions)

        print("Du hast " + action_to_text(user_action))
        print("Gegner hat " + action_to_text(computer_action))

        if user_action == computer_action:
            print("Unentschieden")
            print("Keiner bekommt einen Punkt.")
            score()

        elif user_action == "sc":
            if computer_action == "st":
                print("Stein schleift Schere! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            elif computer_action == "pa":
                print("Schere schneidet Papier! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            elif computer_action == "ec":
                print("Schere köpft Echse! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            else:
                print("Spock zertrümmert Schere! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()

        elif user_action == "st":
            if computer_action == "sc":
                print("Stein schleift Schere! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            elif computer_action == "pa":
                print("Papier bedeckt Stein! Du verlierst")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            elif computer_action == "ec":
                print("Stein zerquetscht Echse! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            else:
                print("Spock verdampft Stein! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()

        elif user_action == "pa":
            if computer_action == "sc":
                print("Schere schneidet Papier! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            elif computer_action == "st":
                print("Papier bedeckt Stein! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            elif computer_action == "ec":
                print("Echse frisst Papier! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            else:
                print("Papier widerlegt Spock! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()

        elif user_action == "ec":
            if computer_action == "sc":
                print("Schere köpft Echse! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            elif computer_action == "st":
                print("Stein zerquetscht Echse! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            elif computer_action == "pa":
                print("Echse frisst Papier! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            else:
                print("Echse vergiftet Spock! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()

        elif user_action == "sp":
            if computer_action == "sc":
                print("Spock zertrümmert Schere! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            elif computer_action == "st":
                print("Spock verdampft Stein! Du gewinnst!")
                print("Du bekommst einen Punkt.")
                user_points += 1
                score()
            elif computer_action == "pa":
                print("Papier widerlegt Spock! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()
            else:
                print("Echse vergiftet Spock! Du verlierst!")
                print("Gegner bekommt einen Punkt.")
                computer_points += 1
                score()

print("Das Spiel wurde beendet.")
