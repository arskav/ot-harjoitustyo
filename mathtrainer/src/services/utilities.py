# Apualiohjelmia
# Tämä tyhjentyi ja on melkein jo turha


def return_to_menu():
    # vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty
    print("X: Lopetetaan harjoittelu ja palataan päävalikkoon")
    print("Mikä tahansa muu: jatka harjoittelua.")
    ans = input("X/muu > ")
    return ans.upper()

def list_to_string(as_list):
    string = " ".join([str(item) + ", " for item in as_list])
    return string[:-2]
