from initialize_databases import initialize_databases


def build():
    """Käytetään ennen sovelluksen käynnistämistä tietokantojen alustukseen."""

    initialize_databases()

if __name__ == "__main__":
    build()
