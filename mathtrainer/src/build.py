from initialize_databases import initialize_databases


def build():
    """Tietokantojen alustus."""

    initialize_databases()

if __name__ == "__main__":
    build()
