"""MARIE – minimale Flask-Anwendung (Durchstich Neo4j → Python → HTML)."""
from pathlib import Path

from flask import Flask, render_template

from db import run_query

FRONTEND = Path(__file__).resolve().parent.parent / "frontend"
app = Flask(
    __name__,
    template_folder=str(FRONTEND / "templates"),
    static_folder=str(FRONTEND / "static"),
)


@app.route("/")
def netzwerk():
    # Testabfrage für den Durchstich; wird nach der Modellkorrektur ersetzt.
    beziehungen = run_query("""
        MATCH (a:Testknoten)-[r]->(b:Testknoten)
        RETURN a.name AS von, type(r) AS typ, b.name AS zu
    """)
    return render_template("netzwerk.html", beziehungen=beziehungen)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
