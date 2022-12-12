def ask_answer_to_question(prompt, mode):

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

    if mode == 'integer':

        if ans[0] == '-':

            input_ok =  ans[1:].isnumeric()

        else:

            input_ok =  ans.isnumeric()

    elif mode == 'nonnegative':

        input_ok =  ans.isnumeric()

    else:

        return ans

    if input_ok:

        return int(ans)

    return None

def cancel():
    """Lopetetaan tehtävien tekeminen.
    """
    print("Lopetus")
    is_correct = False
    is_cancelled = True
    is_finish = False
    return is_correct, is_cancelled, is_finish

def correct_answer(successive_correct, finish):

    successive_correct += 1
    print(f"Peräkkäisiä oikeita {successive_correct}/{finish}")
    is_finish = successive_correct == finish

    return is_finish, successive_correct

def practise_done(drill):
    # Ilmoitus, kun harjoituksen kaikki tasot on tehty
    print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
    print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen,")
    print("valitse uusi käyttäjätunnus.")
    input("Enter paluu päävalikkoon.")

def initiliaze(session):

    drill = session.practise()

    return 0, 0, 0, False, drill


def doing_practise(session, trainee, practise_func):


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



    # Päivitetään käyttäjän kokonaistilanne
    trainee.update_total(correct, tries)

    if session.level() - 1 == session.maxlevel():
        practise_done(drill)
        trainee.practise_finished_append(drill)

    trainee.to_database()
