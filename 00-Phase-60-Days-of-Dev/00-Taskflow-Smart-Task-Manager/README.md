# TaskFlow - Smart Task Manager

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

Eine schlanke Desktop-Anwendung zur intelligenten Aufgabenverwaltung mit Prioritäten, Kategorien und Statistiken.

[Features]() • [Installation]() • [Nutzung]() • [Screenshots]()

</div>

---

## 🎯 Motivation

Als Vater, Ultralearner und Student jongliere ich ständig zwischen Übungsaufgaben, Projekten und persönlichen To-Dos. Bestehende Task-Manager waren entweder:

- Zu komplex (Trello, Asana)
- Zu simpel (Notiz-Apps)
- Kostenpflichtig (Todo ist Premium)

**Meine Lösung:** TaskFlow - eine kostenlose Desktop-App die genau das tut, was ich brauche, ohne Schnickschnack.

## ✨ Features

### Kernfunktionen

- ✅ **Aufgabenverwaltung** - Erstellen, bearbeiten, löschen
- 🎨 **Prioritätssystem** - Hoch (🔴), Mittel (🟡), Niedrig (🟢)
- 🏷️ **Kategorien** - Arbeit, Uni, Persönlich, Shopping
- 🌙 **Dark Mode** - Augenschonende Oberfläche
- 📊 **Statistiken** - Detaillierte Auswertung deiner Produktivität

### Besondere Highlights

- **Intelligente Sortierung** - Automatisch nach Priorität & Datum
- **Schneller Filter** - Aufgaben nach Kategorie filtern
- **CSV Export** - Daten für Backup oder Excel
- **Lokale Datenhaltung** - Keine Cloud, alle Daten bleiben bei dir
- **Doppelklick-Toggle** - Schnell als erledigt markieren

## 🛠️ Tech Stack

```
Backend:     Python 3.11
GUI:         PyQt6
Database:    SQLite3
Design:      Custom Dark Theme
```

**Warum diese Technologien?**

- **PyQt6**: Moderne, plattformübergreifende GUI
- **SQLite**: Lightweight, keine Server-Setup nötig
- **Python**: Schnelle Entwicklung, gut wartbar

## 🚀 Installation

### Voraussetzungen

- Python 3.10 oder höher
- pip (Python Package Manager)

## 📖 Nutzung

### Grundlegende Bedienung

1. **Aufgabe hinzufügen**
    
    - Text eingeben
    - Priorität wählen
    - Kategorie auswählen
    - Enter oder "Hinzufügen" klicken
2. **Aufgabe erledigen**
    
    - Doppelklick auf Task
    - Oder: Task auswählen → "✓ Erledigt"
3. **Filtern & Sortieren**
    
    - Dropdown-Menü nutzen
    - Automatische Sortierung nach Priorität
4. **Statistiken anzeigen**
    
    - Tab "📊 Statistik" öffnen
    - Detaillierte Übersicht deiner Produktivität

### Tastenkombinationen

|Shortcut|Aktion|
|---|---|
|`Enter`|Neue Aufgabe hinzufügen|
|`Del`|Ausgewählte Aufgabe löschen|
|`Doppelklick`|Task als erledigt markieren|

## 📸 Screenshots

### Hauptansicht (Dark Mode)

![Main View](https://claude.ai/chat/screenshots/main_dark.png)

### Statistik-Dashboard

![Statistics](https://claude.ai/chat/screenshots/stats.png)

### Filter & Kategorien

![Categories](https://claude.ai/chat/screenshots/categories.png)

## 📈 Was ich dabei gelernt habe

### Technische Skills

- **GUI-Entwicklung** mit PyQt6
    
    - Event-Handling
    - Custom Styling mit QSS
    - Tab-basierte Navigation
- **Datenbankdesign**
    
    - Normalisierung
    - Context Manager für sichere Connections
    - Effiziente Queries
- **Software-Architektur**
    
    - Separation of Concerns (GUI / Logic / Data)
    - Modularität für einfache Erweiterung

### Herausforderungen & Lösungen

|Problem|Lösung|
|---|---|
|SQLite Connections blieben offen|Context Manager implementiert|
|UI eingefroren bei DB-Operationen|Asynchrone Updates geplant (v2.0)|
|Dark Mode flackerte beim Toggle|Stylesheet-Caching eingebaut|

## 🔮 Roadmap

### Version 2.0 (In Planung)

- [ ] **Recurring Tasks** - Wiederkehrende Aufgaben
- [ ] **Deadlines** - Fälligkeitsdaten mit Benachrichtigungen
- [ ] **Time Tracking** - Wie lange pro Task?
- [ ] **Pomodoro Timer** - Integrierte Fokus-Sessions
- [ ] **Cloud Sync** - Optional via Google Drive
- [ ] **Mobile Companion App** - Flutter-basiert

### Weitere Ideen

- [ ] Drag & Drop Prioritäten ändern
- [ ] Dark/Light Mode automatisch (Systemzeit)
- [ ] Tagging-System
- [ ] Subtasks
- [ ] Collaboration-Features

## 🤝 Mitwirkende willkommen

Hast du Ideen für neue Features? Bugs gefunden?

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 👤 Autor

**[Marc Jannis Nöthen]**

- GitHub: [BSOD-Twins-Error0508@deinusername](https://github.com/BSOD-Twins-Error0508)
- Email: marc.j.noethen@protonmail.com
- LinkedIn: [Dein Profil](https://www.linkedin.com/in/marc-j-n%C3%B6then-b201a315b/)

## 🙏 Danksagungen

- PyQt6 Community für exzellente Dokumentation
- Icons von [Flaticon](https://www.flaticon.com/)
- Inspiration durch moderne Task-Management-Apps

---

<div align="center">

Made with ❤️ and ☕ in Halle (Saale)

</div>