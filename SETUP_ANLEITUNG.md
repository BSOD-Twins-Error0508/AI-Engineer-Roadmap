# 📋 SETUP-ANLEITUNG: Schritt für Schritt

## Übersicht

| Phase | Dauer | Was |
|-------|-------|-----|
| A | 15 min | GitHub Account |
| B | 30 min | Repository erstellen |
| C | 15 min | Erster Content |
| D | Ongoing | Tägliche Routine |

---

# PHASE A: GITHUB ACCOUNT (15 min)

## Schritt 1: Account erstellen/prüfen

1. Gehe zu [github.com](https://github.com)
2. **Neuer Account?** → "Sign up" klicken
3. **Username**: Professionell wählen (z.B. `vorname-nachname`)

## Schritt 2: Profil ausfüllen

1. Gehe zu: `github.com/settings/profile`
2. Ausfüllen:
   - **Name**: Dein echter Name
   - **Bio**: `🎯 Becoming an AI Engineer | Learning in Public | Day 1/1932`
   - **Location**: Deine Stadt
   - **Profilbild**: Professionelles Foto hochladen
3. **Speichern**

---

# PHASE B: REPOSITORY ERSTELLEN (30 min)

## Schritt 3: Repository anlegen

1. Gehe zu [github.com/new](https://github.com/new)
2. Eingeben:
   - **Name**: `AI-Engineer-Roadmap`
   - **Description**: `🚀 My journey to AI Engineer - Learning in Public`
   - **Public**: ✅ Ja
   - **Add README**: ❌ Nein
3. **"Create repository"** klicken

## Schritt 4: Dateien hochladen

### Option A: Web Interface (einfach)

1. Im Repository: Klicke **"uploading an existing file"**
2. ZIP-Datei entpacken
3. ALLE Dateien/Ordner ins Upload-Feld ziehen
4. Commit message: `🎉 Initial commit`
5. **"Commit changes"**

### Option B: Command Line (fortgeschritten)

```bash
git clone https://github.com/DEIN-USERNAME/AI-Engineer-Roadmap.git
cd AI-Engineer-Roadmap
# Dateien reinkopieren
git add .
git commit -m "🎉 Initial commit"
git push
```

## Schritt 5: README personalisieren

1. `README.md` öffnen → Stift-Icon klicken
2. Ersetzen:
   - `DEIN-USERNAME` → Dein GitHub Username
   - `[DEIN HINTERGRUND]` → z.B. "Quereinsteiger aus Marketing"
3. **Commit changes**

---

# PHASE C: ERSTER CONTENT (15 min)

## Schritt 6: Ersten Daily Log schreiben

1. Gehe zu `daily-logs/2025/01-january/`
2. **"Add file"** → **"Create new file"**
3. Name: `2025-01-[HEUTE].md` (z.B. `2025-01-19.md`)
4. Inhalt aus `2025-01-XX-EXAMPLE.md` kopieren
5. Anpassen mit deinen Infos
6. Commit: `📅 Day 001 - Starting my journey`

## Schritt 7: Repository pinnen

1. Gehe zu `github.com/DEIN-USERNAME`
2. **"Customize your pins"** klicken
3. `AI-Engineer-Roadmap` auswählen
4. Speichern

---

# PHASE D: TÄGLICHE ROUTINE (Ongoing)

## Jeden Tag (5-10 min nach dem Lernen):

```
1. Lernen (2h wie geplant)
      ↓
2. Daily Log schreiben
   - Neuer File: daily-logs/2025/XX-month/2025-XX-XX.md
   - Template kopieren & ausfüllen
      ↓
3. Commit & Push
   - Message: "📅 Day XXX - [Kurze Beschreibung]"
```

## Commit Message Konventionen

| Emoji | Bedeutung | Beispiel |
|-------|-----------|----------|
| 📅 | Daily Log | `📅 Day 015 - Finished Clean Code Ch.3` |
| 📖 | Buch-Notizen | `📖 Add notes for Clean Code` |
| 💻 | Projekt | `💻 Start Weather API project` |
| ✅ | Abschluss | `✅ Complete Grokking Algorithms` |
| 📊 | Weekly Review | `📊 Weekly Review W03` |

## Jeden Sonntag: Weekly Review

1. Neuer File: `weekly-reviews/2025-W[XX].md`
2. Template ausfüllen
3. Commit: `📊 Weekly Review W[XX]`

---

# ✅ CHECKLISTE

## Heute erledigen:
- [ ] GitHub Profil optimieren
- [ ] Repository erstellen
- [ ] Dateien hochladen
- [ ] README personalisieren
- [ ] Ersten Daily Log schreiben
- [ ] Repository pinnen

## Diese Woche:
- [ ] Jeden Tag einen Log schreiben
- [ ] Jeden Tag committen

## Nächste Woche:
- [ ] Erste Weekly Review
- [ ] Mit Phase 1 Content starten

---

# ❓ FAQ

**Muss ich jeden Tag committen?**
Ideal ja, aber Qualität > Quantität.

**Was wenn ich einen Tag verpasse?**
Kein Problem! Log am nächsten Tag nachschreiben.

**Wie lang sollen Daily Logs sein?**
5-10 Minuten zum Schreiben reichen.

---

**🎉 Du hast alles was du brauchst. Der erste Commit ist der wichtigste!**
