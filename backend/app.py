"""MARIE – Flask-Anwendung (Stufe 1: serverseitig gerendertes HTML, ohne JavaScript)."""
from pathlib import Path

from flask import Flask, render_template, request

from db import run_query

FRONTEND = Path(__file__).resolve().parent.parent / "frontend"
app = Flask(
    __name__,
    template_folder=str(FRONTEND / "templates"),
    static_folder=str(FRONTEND / "static"),
)

# Testabfragen für die Grundstruktur; werden nach der Modellkorrektur ersetzt.
PERSONEN = "MATCH (p:Testknoten) RETURN p.name AS name ORDER BY name"
VERBINDUNGEN = """
    MATCH (a:Testknoten {name: $person_a})-[r]-(b:Testknoten {name: $person_b})
    RETURN startNode(r).name AS von, type(r) AS typ, endNode(r).name AS zu
"""


@app.route("/")
def start():
    return render_template("start.html", personen=run_query(PERSONEN), person_a="", person_b="")


@app.route("/verbindungen")
def verbindungen():
    person_a = request.args.get("person_a", "")
    person_b = request.args.get("person_b", "")
    meldung = None
    if not person_a or not person_b:
        meldung = "Bitte wähle zwei Personen aus."
    elif person_a == person_b:
        meldung = "Bitte wähle zwei verschiedene Personen aus."
    if meldung:
        return render_template(
            "start.html",
            personen=run_query(PERSONEN),
            person_a=person_a,
            person_b=person_b,
            meldung=meldung,
        )
    beziehungen = run_query(VERBINDUNGEN, {"person_a": person_a, "person_b": person_b})
    return render_template(
        "verbindungen.html",
        personen=run_query(PERSONEN),
        person_a=person_a,
        person_b=person_b,
        beziehungen=beziehungen,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
