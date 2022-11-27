import os
from services.utilities import return_to_menu

FINISH = 2
# Kuinka monen peräkkäisen oikean vastauksen jälkeen siirrytään seuraavalle tasolle.
# Siirtymisehto voi olla valmiissa harjoituksessa joku muukin.


def do_practise(session, correct, tries, cancelled):

    successive_correct = 0
    # Kun peräkkäisiä oikeita vastauksia on (tässä) 2, siirrytään seuraavalle tasolle.
    # Jatkossa siirtymisehtoa voi mutkistaa ja se voi vaihdella eri tasoilla ja harjoituksissa

    # Tämä on vain ohjelmarungon testausta, joten kaikilla tasoilla sama testikysymyssarja
    # jatkokehittelyssä tässä kutsutaan harjoitusten drill tason level kysymysten esittämistä

    while successive_correct < FINISH and not cancelled:

        (is_correct, is_interrupt, is_finish) = fake_question(
            session, successive_correct)
        # successive_correct viittaa nyt lopetusehtoon, mutta aidossa harjoituksessa voi olla
        # muukin lopetusehto kuin peräkkäisten vastausten lukumäärä.
        # Näitä muutetaan meneilläään olevan harjoituksen mukaisesti.
        if is_interrupt:
            cancelled = True
            break

        session.new_attempt()
        tries += 1
        # Ainakin yritetty vastata
        if not is_correct:
            print("Väärin")
        else:
            print("Oikein")
            session.correct_up()
            correct += 1
            successive_correct += 1

        if is_finish:
            # Lopetusehdon toteutuessa siirrytään seuraavalle tasolle
            # Tässä testauksessa riittää vastata kaksi kertaa 1,
            # joka tulkitaan oikeaksi vastaukseksi

            # siirrytään seuravalla tasolle
            session.level_up()

            if session.level() <= session.maxlevel():
                if return_to_menu():
                    cancelled = True
                    break



    return correct, tries, cancelled

# TO DO varsinaisen harjoituksen koodaaminen


def fake_question(session, successive_correct):
    """Testausta varten"""
    os.system('clear')
    print("Nämä eivät ole todellisia tehtäviä, vaan leikkikysymyksiä ohjelmarungon testaamiseksi.")
    print(f"Harjoitus 1, taso {session.level()}")
    print("---------------------------------------")
    print(session)
    print("Peräkkäisiä oikeita", successive_correct)
    print("Vastaamalla muuta kuin 0 tai 1 keskeytät harjoituksen tekemisen")

    answer = input(
        " testi, vastaa 0 tai 1 : 0 väärin, 1 oikein, muu keskeytys > ")

    is_correct = (answer == str(1))
    is_interrupt = (answer not in [str(0), str(1)])
    is_finish = is_correct and successive_correct == FINISH - 1
    # Nämä todellisessa tilanteessa määräytyvät meneillä olevasta harjoituksesta ja kysymyksestä
    return (is_correct, is_interrupt, is_finish)
