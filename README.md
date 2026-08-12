# MARIE – Meeting Artists in Research and Interdisciplinary Education

Netzwerkvisualisierung kunsthistorischer Beziehungen am Fallbeispiel Paula Modersohn-Becker.

Dieses Repositorium enthält den funktionalen Prototyp, der im Rahmen einer Masterarbeit im Studiengang *Digitale Methodik in den Geistes- und Kulturwissenschaften* (Johannes Gutenberg-Universität Mainz) entstanden ist.

🔗 Landingpage: [ma-rie.eu](https://www.ma-rie.eu/) ([Repository](https://github.com/Liztomania/MARIE-landing)))
🔗 Prototyp: *ma-rie.eu/prototype (folgt)*

### Inhalt

Das Repositorium bildet die Prüfungsleistungen der Masterarbeit ab:

- <u>Thesis:</u> Die schriftliche Ausarbeitung liegt im Ordner [`thesis/`](./thesis) als PDF vor.
- <u>Data:</u> Datengrundlage und aufbereitete Datensätze liegen in [`data/`](./data). Die Struktur und Herkunft der Daten ist im [DataDictionary.md](./data/DataDictionary.md) tabellarisch erläutert; Importbefehle und Beispiel-Cypher-Queries sind in [`backend/Queries.md`](./backend/Queries.md) dokumentiert.
- <u>Prototyp/Website:</u> Quellcode der interaktiven Netzwerkvisualisierung liegt in [`frontend/`](./frontend), die API-Anbindung an Neo4j in [`backend/`](./backend).
- <u>Poster:</u> Liegt als PNG/PDF in [`poster/`](./poster) vor.

## Projektkontext

MARIE macht künstlerische und persönliche Beziehungen zwischen historischen Akteur:innen sichtbar, die in normdatenbasierten Systemen wie GND oder Wikidata nicht primär als Netzwerk erschlossen sind. Als Fallbeispiel dient ein Sechs-Personen-Netzwerk um Paula Modersohn-Becker:

- Paula Modersohn-Becker
- Rainer Maria Rilke
- Clara Rilke-Westhoff
- Camille Claudel
- Bernhard Hoetger
- Auguste Rodin

## Datenquellen

- **GND** (via [lobid.org](https://lobid.org) / DNB-Turtle-Endpunkt) – Personendaten und Basisrelationen
- **Korrespondenz** (exemplarisch, 2 Briefe) – manuell aufbereitet?? Oder: erschlossen über [correspSearch](https://correspsearch.net/) bzw. Kalliope
- **Ausstellungskataloge** (exemplarisch, 2 Kataloge) – manuell aufbereitete Werk- und Ausstellungsbezüge

Die Datenmodellierung folgt zunächst einem Entity-Relationship-Modell, auf dessen Basis die Ontologie-Entscheidung (CIDOC CRM, Version 7.1.3) begründet wird. Modellierung und ER-Diagramme wurden mit [Protégé](https://protege.stanford.edu/) erstellt und liegen in [`ontology/`](./ontology).

## Software

| Bereich | Technologie | Installation |
|---|---|---|
| Datenbank | [Neo4j Aura](https://neo4j.com/cloud/aura/) (Free Tier) | [Anleitung](https://neo4j.com/docs/aura/auradb/getting-started/) |
?? | API-Schicht | Serverless Functions ([Vercel](https://vercel.com/) / [Netlify](https://www.netlify.com/)) | [Vercel Docs](https://vercel.com/docs) | ??
| Visualisierung | [Cytoscape.js](https://js.cytoscape.org/) | [Docs](https://js.cytoscape.org/#getting-started) |
| Datenmodellierung | [Protégé](https://protege.stanford.edu/) | [Download](https://protege.stanford.edu/software.php) |

## Repository-Struktur

```
├── backend/  # API-Funktionen, Cypher-Queries (Queries.md)
├── data/  # Rohdaten & aufbereitete Datensätze, DataDictionary.md
├── docs/  # Styleguide, Architektur-Dokumentation, Screenshots
├── frontend/  # HTML/CSS/JS, Cytoscape.js-Visualisierung
├── ontology/  # Protégé-Dateien, ER-/Ontologie-Diagramme
├── poster/  # Poster (PNG/PDF)
└── thesis/  # Schriftliche Ausarbeitung (PDF)
```

## Setup

*(wird ergänzt, sobald Backend und Frontend eingerichtet sind)*

```bash
# Repository klonen
git clone https://github.com/<username>/MARIE.git
cd MARIE

# Umgebungsvariablen einrichten
cp .env.example .env
# .env mit eigenen Neo4j-Aura-Zugangsdaten befüllen
```

## Autorin

Elisabeth Pilhofer – Masterarbeit, betreut von Prof. Dr. phil. Franziska Klemstein (HTWK Leipzig) und Prof. Dr. phil. Gabriele Schmid (HKS Ottersberg).

## Lizenz und Zitation

*(Lizenz noch final festzulegen – vorgesehen: MIT für den Code, CC-BY für Daten/Dokumentation)*

Zitationsvorschlag (Chicago 17th ed.):
Pilhofer, Elisabeth. *MARIE – Meeting Artists in Research and Interdisciplinary Education. Eine Netzwerkvisualisierung am Fallbeispiel Paula Modersohn-Becker.* Masterarbeit, Johannes Gutenberg-Universität Mainz, 2027.
