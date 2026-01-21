\# TaskFlow - Smart Task Manager



<div align="center">



!\[Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)

!\[License](https://img.shields.io/badge/License-MIT-green.svg)

!\[Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)



Eine schlanke Desktop-Anwendung zur intelligenten Aufgabenverwaltung mit Prioritäten, Kategorien und Statistiken.



\[Features](#-features) •

\[Installation](#-installation) •

\[Nutzung](#-nutzung) •

\[Screenshots](#-screenshots)



</div>



---



\## 🎯 Motivation



Als Student und Freelancer jongliere ich ständig zwischen Uni-Aufgaben, Projekten und persönlichen To-Dos. Bestehende Task-Manager waren entweder:

\- Zu komplex (Trello, Asana)

\- Zu simpel (Notiz-Apps)

\- Kostenpflichtig (Todoist Premium)



\*\*Meine Lösung:\*\* TaskFlow - eine kostenlose Desktop-App die genau das tut, was ich brauche, ohne Schnickschnack.



\## ✨ Features



\### Kernfunktionen

\- ✅ \*\*Aufgabenverwaltung\*\* - Erstellen, bearbeiten, löschen

\- 🎨 \*\*Prioritätssystem\*\* - Hoch (🔴), Mittel (🟡), Niedrig (🟢)

\- 🏷️ \*\*Kategorien\*\* - Arbeit, Uni, Persönlich, Shopping

\- 🌙 \*\*Dark Mode\*\* - Augenschonende Oberfläche

\- 📊 \*\*Statistiken\*\* - Detaillierte Auswertung deiner Produktivität



\### Besondere Highlights

\- \*\*Intelligente Sortierung\*\* - Automatisch nach Priorität \& Datum

\- \*\*Schneller Filter\*\* - Aufgaben nach Kategorie filtern

\- \*\*CSV Export\*\* - Daten für Backup oder Excel

\- \*\*Lokale Datenhaltung\*\* - Keine Cloud, alle Daten bleiben bei dir

\- \*\*Doppelklick-Toggle\*\* - Schnell als erledigt markieren



\## 🛠️ Tech Stack



```

Backend:     Python 3.11

GUI:         PyQt6

Database:    SQLite3

Design:      Custom Dark Theme

```



\*\*Warum diese Technologien?\*\*

\- \*\*PyQt6\*\*: Moderne, plattformübergreifende GUI

\- \*\*SQLite\*\*: Lightweight, keine Server-Setup nötig

\- \*\*Python\*\*: Schnelle Entwicklung, gut wartbar



\## 🚀 Installation



\### Voraussetzungen

\- Python 3.10 oder höher

\- pip (Python Package Manager)



\### Schritt-für-Schritt



```bash

\# 1. Repository klonen

git clone https://github.com/deinname/TaskFlow.git

cd TaskFlow



\# 2. Virtual Environment (empfohlen)

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate



\# 3. Dependencies installieren

pip install -r requirements.txt



\# 4. Anwendung starten

python src/main.py

```



\### Alternative: Standalone Executable

\*(Coming soon - PyInstaller Build)\*



\## 📖 Nutzung



\### Grundlegende Bedienung



1\. \*\*Aufgabe hinzufügen\*\*

&nbsp;  - Text eingeben

&nbsp;  - Priorität wählen

&nbsp;  - Kategorie auswählen

&nbsp;  - Enter oder "Hinzufügen" klicken



2\. \*\*Aufgabe erledigen\*\*

&nbsp;  - Doppelklick auf Task

&nbsp;  - Oder: Task auswählen → "✓ Erledigt"



3\. \*\*Filtern \& Sortieren\*\*

&nbsp;  - Dropdown-Menü nutzen

&nbsp;  - Automatische Sortierung nach Priorität



4\. \*\*Statistiken anzeigen\*\*

&nbsp;  - Tab "📊 Statistik" öffnen

&nbsp;  - Detaillierte Übersicht deiner Produktivität



\### Tastenkombinationen



| Shortcut | Aktion |

|----------|--------|

| `Enter` | Neue Aufgabe hinzufügen |

| `Del` | Ausgewählte Aufgabe löschen |

| `Doppelklick` | Task als erledigt markieren |



\## 📸 Screenshots



\### Hauptansicht (Dark Mode)

!\[Main View](screenshots/main\_dark.png)



\### Statistik-Dashboard

!\[Statistics](screenshots/stats.png)



\### Filter \& Kategorien

!\[Categories](screenshots/categories.png)



\## 📈 Was ich dabei gelernt habe



\### Technische Skills

\- \*\*GUI-Entwicklung\*\* mit PyQt6

&nbsp; - Event-Handling

&nbsp; - Custom Styling mit QSS

&nbsp; - Tab-basierte Navigation

&nbsp; 

\- \*\*Datenbankdesign\*\*

&nbsp; - Normalisierung

&nbsp; - Context Manager für sichere Connections

&nbsp; - Effiziente Queries



\- \*\*Software-Architektur\*\*

&nbsp; - Separation of Concerns (GUI / Logic / Data)

&nbsp; - Modularität für einfache Erweiterung



\### Herausforderungen \& Lösungen



| Problem | Lösung |

|---------|--------|

| SQLite Connections blieben offen | Context Manager implementiert |

| UI eingefroren bei DB-Operationen | Asynchrone Updates geplant (v2.0) |

| Dark Mode flackerte beim Toggle | Stylesheet-Caching eingebaut |



\## 🔮 Roadmap



\### Version 2.0 (In Planung)

\- \[ ] \*\*Recurring Tasks\*\* - Wiederkehrende Aufgaben

\- \[ ] \*\*Deadlines\*\* - Fälligkeitsdaten mit Benachrichtigungen

\- \[ ] \*\*Time Tracking\*\* - Wie lange pro Task?

\- \[ ] \*\*Pomodoro Timer\*\* - Integrierte Fokus-Sessions

\- \[ ] \*\*Cloud Sync\*\* - Optional via Google Drive

\- \[ ] \*\*Mobile Companion App\*\* - Flutter-basiert



\### Weitere Ideen

\- \[ ] Drag \& Drop Prioritäten ändern

\- \[ ] Dark/Light Mode automatisch (Systemzeit)

\- \[ ] Tagging-System

\- \[ ] Subtasks

\- \[ ] Collaboration-Features



\## 🤝 Mitwirkende willkommen



Hast du Ideen für neue Features? Bugs gefunden? 



1\. Fork das Repository

2\. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)

3\. Commit deine Changes (`git commit -m 'Add some AmazingFeature'`)

4\. Push zum Branch (`git push origin feature/AmazingFeature`)

5\. Öffne einen Pull Request



\## 📝 Lizenz



Dieses Projekt ist unter der MIT Lizenz veröffentlicht. Siehe \[LICENSE](LICENSE) für Details.



\## 👤 Autor



\*\*\[Dein Name]\*\*

\- GitHub: \[@deinusername](https://github.com/deinusername)

\- Email: deine.email@example.com

\- LinkedIn: \[Dein Profil](https://linkedin.com/in/deinprofil)



\## 🙏 Danksagungen



\- PyQt6 Community für exzellente Dokumentation

\- Icons von \[Flaticon](https://www.flaticon.com)

\- Inspiration durch moderne Task-Management-Apps



---



<div align="center">

Made with ❤️ and ☕ in Halle (Saale)

</div>

