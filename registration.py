registrations = []
registrations_completes = False

def register_user(firstName, lastName):
    global registrations_completes
    if len(registrations) < 5:
        registrations.append([firstName, lastName])
        print(f"{firstName} {lastName} a été inscrit(e) avec succès!")
    elif not registrations_completes:
        print("les incriptions sont complètes. Les cinq premiers candidats sont déja sélectionnés")
        registrations_completes = True
        print("_" * 40)       

def display_selection():
    if len(registrations) == 0:
        print("aucun utilisateur n'a été inscrit")
    else:
        selections = registrations[:5] #prendre les 5 premiers incrits
        print("les candidats sélectionnés pour la bourse sont :")
        for candidate in selections:
            print(f"- {candidate}")

#simulation
register_user("mouhamed", "fall")
register_user("john", "harris")
register_user("fatou", "diop")
register_user("amadou", "ndiaye")
register_user("fallou", "tall")
register_user("justin", "manga")
register_user("edouard", "kama")


display_selection()