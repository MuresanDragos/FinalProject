import random

def piatra_hartie_foarfeca():
    alegerea_utilizatorului = input("Introdu alegerea ta (piatra, hartie, foarfeca): ").lower()
    alegerea_calculatorului = random.choice(["piatra", "hartie", "foarfeca"])
    print("Calculatorul a ales:", alegerea_calculatorului)

    if alegerea_utilizatorului == alegerea_calculatorului:
        print("Este remiză!")
    elif (alegerea_utilizatorului == "piatra" and alegerea_calculatorului == "foarfeca") or \
         (alegerea_utilizatorului == "hartie" and alegerea_calculatorului == "piatra") or \
         (alegerea_utilizatorului == "foarfeca" and alegerea_calculatorului == "hartie"):
        print("Felicitări! Ai câștigat!")
    else:
        print("Ne pare rău! Calculatorul a câștigat!")


piatra_hartie_foarfeca()

