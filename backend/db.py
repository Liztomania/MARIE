"""MARIE – Skript 1: Verbindungsschicht zu Neo4j.

Modellunabhängig: liest die Zugangsdaten aus backend/.env,
stellt die Verbindung her und führt Cypher-Abfragen aus.
Direkt gestartet (python db.py) führt es einen Verbindungstest aus.
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase, RoutingControl

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH)


def _env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"'{name}' fehlt in {ENV_PATH}")
    return value


NEO4J_URI = _env("NEO4J_URI")
NEO4J_USER = _env("NEO4J_USER")
NEO4J_PASSWORD = _env("NEO4J_PASSWORD")
NEO4J_DATABASE = _env("NEO4J_DATABASE")

_driver = None


def get_driver():
    """Gibt den Treiber zurück; legt ihn beim ersten Aufruf an."""
    global _driver
    if _driver is None:
        _driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return _driver


def run_query(query, params=None, write=False):
    """Führt eine Cypher-Abfrage aus und gibt eine Liste von Dictionaries zurück."""
    records, _, _ = get_driver().execute_query(
        query,
        parameters_=params or {},
        database_=NEO4J_DATABASE,
        routing_=RoutingControl.WRITE if write else RoutingControl.READ,
    )
    return [record.data() for record in records]


def close():
    """Schließt die Verbindung."""
    global _driver
    if _driver is not None:
        _driver.close()
        _driver = None


def check_connection():
    """Prüft die Verbindung; gibt Serverversion und Knotenzahl zurück."""
    driver = get_driver()
    driver.verify_connectivity()
    agent = driver.get_server_info().agent
    anzahl = run_query("MATCH (n) RETURN count(n) AS anzahl")[0]["anzahl"]
    return agent, anzahl


if __name__ == "__main__":
    try:
        agent, anzahl = check_connection()
        print(f"Verbindung OK: {agent}, Datenbank '{NEO4J_DATABASE}', {anzahl} Knoten")
    finally:
        close()
