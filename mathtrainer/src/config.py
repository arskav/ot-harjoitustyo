import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:

    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

except FileNotFoundError:
    print("Tiedostoa .env ei löydy.")
    print("Annetaan muuttujille oletusarvot.")

DATABASE_SESSIONS = os.getenv("DATABASE_SESSIONS") or "./data/sessiondata.sqlite"
DATABASE_USERS = os.getenv("DATABASE_USERS") or "./data/userdata.sqlite"
"""Tietokannat harjoitussessioille ja käyttäjille."""
