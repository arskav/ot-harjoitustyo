def ask_answer_to_question(prompt, mode):
    """Uudempi versio tavasta kysyä vastaus.

    Args:
        prompt (string): kehote inputissa
        mode (string): hyväksyttävän vastauksen tyyppi.

    Returns:
        Boolean: onko vastaus oikean tyyppinen.
    """

    if mode == 'integer':

        print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    elif mode == 'nonnegative':
        print("Vastaus on kokonaisluku 0, 1, 2, 3, ...")
    else:
        pass

    print("Muu vastaus (esim. pelkkä Enter) keskeyttää tehtävän suorittamisen.")

    ans =  input(prompt)

    answer = check_if_input_ok(ans, mode)

    return answer

def check_if_input_ok(ans, mode):
    """Tarkistaa, onko vastaus oikean tyyppinen.

    Args:
        ans (string): annettu vastaus merkkijonoja.
        mode (string): hyväksyttävän vastauksen tyyppi.

    Returns:
        string: vastaus lukuna, jos oikean tyyppinen,
            muuten None
    """

    if mode == 'integer':

        if ans[0] == '-':

            input_ok =  ans[1:].isnumeric()

        else:

            input_ok =  ans.isnumeric()

    elif mode == 'nonnegative':

        input_ok =  ans.isnumeric()

    else:

        input_ok = False

    if input_ok:

        return int(ans)

    return None

def cancel():
    """Lopetetaan harjoituksen tekeminen.

    Returns:
        (False, True, False): ei oikein, keskeytetty, ei lopussa
    """
    print("Lopetus")

    return False, True, False

def correct_answer(successive_correct, finish):
    """Tarkastaa, onko peräkkäisiä oikeita vastauksia niin monta,
    että lopetusehto toteutuu.

    Args:
        successive_correct (int): peräkkäisten oikeiden vastausten lukumäärä.
        finish (int): kuinka monta peräkkäistä oikeaa riittää lopetukseen,

    Returns:
        (Boolean, int): toteutuuko lopetusehto, päivitetty perkkäisten oikeiden vastausten lkm.
    """

    successive_correct += 1
    print(f"Peräkkäisiä oikeita {successive_correct}/{finish}")
    is_finish = successive_correct == finish

    return is_finish, successive_correct

def practise_done(drill):
    """Ilmoitus, kun harjoituksen kaikki tasot on tehty."""

    print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
    print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen,")
    print("valitse uusi käyttäjätunnus.")
    input("Jatka >> ")

def initiliaze(session):
    """Alkuarvot aloitettaessa harjoitussessioni.

    Args:
        session (MathTrainerSession): aloitettava harjoitussessioni.

    Returns:
        oikeat vastaukset = 0, yritykset = 0, peräkkäiset oikeat = 0,
        peruutettu = False, harjoituksen numero
    """

    drill = session.practise()

    return 0, 0, 0, False, drill


def doing_practise(session, trainee, practise_func):
    """Suoritetaan harjoituksen yhtä tasoa. Tallennetaan
    harjoituksen tiedot, kun taso tehty loppuun.

    Args:
        session (MathTrainerSession): meneillään oleva harjoitussessio.
        trainee (MathTrainerUser): käyttäjä.
        practise_func: funktio, joka valitsee harjoituksen.
    """


    correct, tries, successive_correct, is_cancelled, drill = initiliaze(session)

    while session.ongoing():

        print("---------------------------------------")
        print(session)

        is_correct, is_cancelled, is_finish = practise_func(
            successive_correct, session.level())

        if is_cancelled:
            session.cancel()
            break

        session.new_attempt()
        tries += 1

        successive_correct, correct = session.correct_or_not(
            is_correct, successive_correct, correct
            )

        if is_finish:
            successive_correct = 0
            session.finish()

    trainee.update_total(correct, tries)

    if session.level() - 1 == session.maxlevel():
        practise_done(drill)
        trainee.practise_finished_append(drill)

    trainee.to_database()
