# Claude Code Tutorial — Nick Saraev

> YouTube: https://youtu.be/QoQBzR1NIqI
> Doku: code.claude.com/docs

---

## Kapitel 1: Einführung (0:00)

- Nick Saraev nutzt Claude Code täglich für ein Business mit über 4 Mio. $/Jahr Gewinn
- Lehrt über 2.000 Leute Claude Code (privat und beruflich)
- **Kein technischer Hintergrund nötig** — der Kurs baut Konzepte schrittweise auf
- Kursinhalt: Setup, IDEs, CLAUDE.md, Web-App bauen, Modes, Context Management, Slash Commands, Hooks, Skills, MCP, Plugins, Subagents, Worktrees, Deployment

## Kapitel 2: Kursübersicht (1:08)

Vollständige Themenübersicht des Kurses:
1. **Basics:** Download, Setup, IDEs
2. **Erste Web-App bauen** (learning by doing)
3. **`.claude/`-Verzeichnis** und Subagents-Ordner
4. **Modes:** Plan Mode, "Dangerously Skip Permissions", sicherer Umgang
5. **Komplexe Projekte** mit Plan Mode
6. **Context Management:** Effizient arbeiten, Context Rot vermeiden, Prompts strukturieren
7. **Alle Slash Commands** erklärt
8. **Hooks:** Custom Scripts, die automatisch vor/nach jedem Tool Call feuern
9. **Skills:** Skill-Dateien, die Claude Code in spezialisierte Agenten verwandeln
10. **MCP (Model Context Protocol):** Setup + automatisierte Systeme (E-Mail-Manager, Buchhaltung etc.)
11. **Plugins & Marketplaces**
12. **Chrome DevTools Integration:** Daten von Quellen ohne API sammeln
13. **Subagents** mit eingeschränktem Tool-Zugriff
14. **Agent Teams** und produktiver Einsatz
15. **Worktrees & Session Mobility:** Parallele Sessions ohne Nachteile
16. **Scaling & Deployment:** Modal Webhooks, GitHub Actions, Claude Code on the Web

## Kapitel 3: Claude Code einrichten (2:56)

- **Mindestens Pro-Plan nötig** ($17/Monat) — kein Free-Plan-Zugang
- Nick schätzt seinen Produktivitätsgewinn auf 10.000–15.000 $/Monat
- **Installation Terminal:**
  - Mac/Linux/WSL: `curl`-Befehl aus der Doku kopieren und ausführen
  - Windows: PowerShell oder CMD nutzen
  - Danach einfach `claude` ins Terminal tippen
- **Login:** `/login` eingeben, mit Pro/Max/Team/Enterprise-Abo authentifizieren
- **Kernvorteil:** Claude Code läuft lokal auf deinem Computer — kann Dateien ändern, Scripts schreiben, Ordner umstrukturieren, PC aufräumen etc.
- **Doku-Ressource:** code.claude.com/docs (in jeder Sprache verfügbar)

## Kapitel 4: Terminal vs. GUI (8:05)

### Terminal-Oberfläche erklärt:
- **Oben links:** Claude Code Logo + Version
- **Darunter:** Aktuelles Modell (z.B. Opus 4.6) und Plan (Pro/Max etc.)
- **Working Directory:** Der Ordner, in dem Claude Code gerade arbeitet
- **Modes:** Mit `Shift+Tab` durchschalten (z.B. Bypass Permissions)
- **Status Line:** Anpassbar — kann Token-Zähler, Farben etc. anzeigen
- **Thinking-Wörter:** Claude zeigt lustige Begriffe beim Denken ("finagling", "rumpeting" etc.) — anpassbar

### Tokens & Context:
- **Token ≈ Wort** (etwas mehr — "Hey, how's it going?" = ca. 6–7 Tokens statt 4 Wörter)
- **Context-Anzeige:** 0–100% — zeigt, wie voll das Konversations-Fenster ist
- **Automatische Komprimierung:** Claude Code verdichtet alte Nachrichten automatisch, um im Fenster zu bleiben
- **Context Management = der größte Flaschenhals** aktuell

### Empfehlung:
- Terminal bietet mehr Funktionalität (mehrere Sessions nebeneinander, schnellere Refresh-Zeiten)
- Aber GUI ist einfacher für Einsteiger

## Kapitel 5: Was ist eine IDE? (12:27)

**IDE = Integrated Development Environment** — drei Dinge in einem:
1. **Datei-Explorer** (wie Windows Explorer / Mac Finder)
2. **Text-Editor** (wie Notepad)
3. **AI-Chat-Widget** (wie ChatGPT)

### Die zwei großen IDEs:
| | VS Code | Antigravity |
|---|---|---|
| Hersteller | Microsoft | Google |
| Status | Etabliert, erweiterbar | Neuer, moderner, AI-fokussiert |
| Basis | Original | Auf VS Code aufgebaut |
| Empfehlung | Gut zum Starten | "VS Code 2.0", wird im Kurs bevorzugt |

## Kapitel 6: VS Code einrichten (13:54)

- Download von der offiziellen VS Code Website
- **Claude Code als Extension installieren:**
  - Links auf die Blöcke (Extensions) klicken
  - "Claude Code" suchen
  - **Nur die offizielle Anthropic-Extension** mit Häkchen installieren (Achtung: Malware-Risiko bei inoffiziellen!)
- **Zwei Wege Claude Code zu nutzen:**
  - Agent-Panel rechts (empfohlen für Einsteiger)
  - Terminal-Integration (Claude-Logo oben)

### Permission Modes in der GUI:
- **Ask before edits:** Fragt vor jeder Änderung (sicher, aber langsam)
- **Edit automatically:** Ändert ohne zu fragen
- **Bypass permissions:** Volle Freiheit (Nick's Präferenz für Wissensarbeit)

### Kontext-Dateien:
- Offene Dateien im Editor werden automatisch als Kontext mitgegeben
- Datei-Inhalt wird erst gelesen, wenn Claude aktiv darauf zugreift (spart Tokens)

## Kapitel 7: Antigravity einrichten (19:12)

- Download von antigravity.google
- Gleiche Struktur wie VS Code (Explorer links, Editor Mitte, Agent rechts)
- Claude Code Extension genauso installieren
- **Tipp:** Standard-Agent (Gemini) durch Claude Code ersetzen — auf Claude-Icon klicken
- Antigravity ist ein Google-Produkt, daher wird Gemini standardmäßig gepusht

## Kapitel 8: Erste Web-App bauen (24:10)

### Kernaussage:
- Claude Code kann **award-winning Websites in unter 10 Minuten** bauen
- Nicht übertrieben — Nick hat selbst dutzende so gebaut
- **godly.website** = Inspiration für hochwertiges Design

### Was du lernst:
1. Wie CLAUDE.md die Outputs beeinflusst
2. Die drei Methoden für Website-Design
3. Deployment-Grundlagen

## Kapitel 9: CLAUDE.md — das Projekt-Gehirn (25:33)

### Wie CLAUDE.md funktioniert:
- Wird **automatisch als allererster Prompt** in jede Konversation injiziert
- Noch BEVOR du deine erste Nachricht schreibst
- Steuert die "Richtung" aller folgenden Antworten

### Die Schiffs-Analogie:
- Stell dir vor, du fährst mit einem Schiff von der US-Ostküste nach Westafrika (~10.000 km)
- Wenn du am Hafen nur 1° daneben liegst, landest du tausende Kilometer vom Ziel entfernt
- **CLAUDE.md = die initiale Ausrichtung deines Schiffs**
- Je präziser die CLAUDE.md, desto genauer alle Ergebnisse
- Minimiert den "Winkel" der möglichen Abweichungen

### Best Practices:
- **Prägnant und klar** formulieren
- Die **Grenzen und den Zweck** des Workspace definieren
- Man könnte den Inhalt auch jedes Mal manuell eintippen — CLAUDE.md automatisiert das einfach
- CLAUDE.md = Capital C-L-A-U-D-E.md im Projekt-Root

## Kapitel 10: Drei Ansätze für Website-Design (30:55)

### Ansatz 1: Design + Screenshot-Loop (empfohlen)
1. Inspirations-Website finden
2. **Ganzseitigen Screenshot machen:** `Ctrl+Shift+I` (Inspect) → Dimension auf 1920x1080 → `Ctrl+Shift+P` → "Capture full size screenshot"
3. Screenshot verkleinern (< 4–5 MB, z.B. via iloveimage.com)
4. CSS-Styles kopieren: Body-Tag → Rechtsklick → "Copy styles"
5. Screenshot + Styles in Claude Code einfügen
6. Claude baut die Seite, macht Screenshots, vergleicht, verbessert iterativ → 80% → 90% → 95% → 99%

### Ansatz 2: Voice Transcript Dump
- FN-Taste halten → Spracheingabe (200 Wörter/Min vs. 50–70 Wörter/Min tippen = 3x schneller)
- Alles was du auf der Website willst, einfach diktieren
- Nicht perfekt beim ersten Mal, aber schnelles Hin-und-Her-Iterieren

### Ansatz 3: Komponenten-Bibliotheken
- z.B. **21st.dev** — Designer haben fertige Website-Komponenten erstellt
- "Copy Prompt" klicken → in Claude Code einfügen → Komponente wird reproduziert
- Gut für einzelne Elemente (Buttons, Cards, Animationen), aber Ansatz 1 ist effizienter für ganze Seiten

### Bauen vs. Deployen:
- **Bauen** = lokal auf deinem Computer
- **Deployen** = ins Internet stellen (Netlify, Vercel, Modal etc.)
- Deployment kommt in späteren Modulen

## Kern-Philosophie: Task → Do → Verify (39:35)

**Das wichtigste Konzept im ganzen Kurs:**

Die meisten Leute machen: Aufgabe → Erledigen → nächste Aufgabe → Erledigen...

**Besser:** Aufgabe → Erledigen → **Ergebnis prüfen** → Verbessern → Prüfen → ...

- Claude Code die Möglichkeit geben, seine eigenen Ergebnisse zu verifizieren (Screenshots, Tests)
- **KI ist nicht perfekt beim ersten Versuch** — aber extrem schnell im Iterieren
- Mensch: Hohe Qualität beim ersten Versuch, aber 5 Stunden Arbeit
- KI: 80% beim ersten Versuch, aber in 5 Minuten bei 99%
- **Der wahre Wert von KI = Geschwindigkeit beim Iterieren**, nicht Perfektion beim ersten Mal

## Kapitel 11: Verifikation in der Praxis + Paralleles Arbeiten (41:53)

### Parallele Websites bauen:
- Mehrere Antigravity/VS Code Fenster gleichzeitig öffnen, jedes mit eigener Claude Code Instanz
- So viele Instanzen wie Token-Budget erlaubt
- **Praktisches Beispiel:** Zwei Websites gleichzeitig designen, am Ende die beste auswählen
- Im Terminal noch effizienter — 5, 10 oder 20 Instanzen gleichzeitig möglich

### Workflow paralleles Arbeiten:
1. Erste Instanz: Screenshot-Loop läuft automatisch
2. Zweite Instanz: Anderes Design parallel
3. Per **Voice Dump** Feedback geben (FN-Taste → diktieren)
4. Claude macht iterative Verbesserungen basierend auf deinem Feedback

### Tipps für Multi-Tab-Arbeit:
- **Faustregel:** Wenn Claude mehr als 10–20% der Zeit auf dich wartet → zu viele Tabs offen
- Nick's Maximum: 3–4 Tabs gleichzeitig
- **Hook-Chime:** Einen Sound einrichten, der ertönt wenn Claude fertig ist (verschiedene Sounds für verschiedene Fenster)
- Ist eine erlernte Fähigkeit, kommt mit der Zeit

### Mobile Optimierung:
- Gleicher Prozess wie Desktop, nur mit mobilem Screenshot
- Oder einfach sagen: "Mach das mobile-optimiert"

## Kapitel 12: Fortgeschrittene Funktionen (54:43)

- Weniger als 10% der Claude Code Nutzer kennen diese Features
- Ab hier: `.claude`-Verzeichnis, Rules, Agents, Skills, Memory, Permission Modes, Plan Mode

## Kapitel 13: Das .claude-Verzeichnis (55:17)

### Was ist `.claude`?
- Versteckter Ordner (Punkt-Konvention = unsichtbar im File Explorer)
- Enthält 10–15 fortgeschrittene Features zur Anpassung von Claude Code

### Struktur eines voll ausgestatteten `.claude`-Ordners:

```
.claude/
├── settings.json          # Team-Permissions + Hooks
├── settings.local.json    # Lokale Settings (nicht auf GitHub gepusht)
├── CLAUDE.md              # Projekt-CLAUDE.md
├── CLAUDE.local.md        # Lokale Version (git-ignored)
├── agents/                # Sub-Agenten definieren
├── skills/                # Skills (= automatisierte Workflows)
└── rules/                 # Regeln aufgeteilt nach Thema
```

- `.local` = bleibt auf deinem Computer, wird nicht zu GitHub gepusht (für sensible Daten)
- Die meisten Leute entwickeln diese Dateien zusammen mit Claude, nicht alleine

### Rules — CLAUDE.md aufteilen:
- Statt einer riesigen CLAUDE.md → in thematische Regeln aufteilen
- z.B. `rules/workflow.md`, `rules/design.md`, `rules/tech-defaults.md`
- **Vorteile:**
  - Granularere Kontrolle (Workflow ändern ohne Design-Regeln zu berühren)
  - Bessere Übersicht bei langen CLAUDE.md (manche haben 10.000+ Wörter)
  - Bei Teamarbeit: verschiedene Leute bearbeiten verschiedene Regeln
  - Leichter zu erkennen, was nicht mehr gebraucht wird

### Drei Ebenen von CLAUDE.md:

| Ebene | Pfad | Anwendung |
|---|---|---|
| **Global** (persönlich) | `~/.claude/CLAUDE.md` | Gilt für ALLE Workspaces |
| **Lokal** (pro Projekt) | `.claude/CLAUDE.md` im Workspace | Gilt nur für dieses Projekt |
| **Enterprise** | System-Level | Für Unternehmenslizenz (99,9% brauchen das nicht) |

- Global überschreibt Lokal bei Konflikten
- **Team-Einsatz:** Director hat globale Regeln, einzelne Mitarbeiter haben lokale

### `/init` — Automatische CLAUDE.md generieren:
- In jedem neuen Ordner: `/init` ausführen
- Claude liest alle Dateien, erkennt Muster, erstellt automatisch eine CLAUDE.md
- **Spart massiv Tokens**, weil Claude nicht jedes Mal alle Dateien lesen muss
- Beschreibung der Ordnerstruktur allein = 90% der Arbeit

### CLAUDE.md Best Practices (Do's & Don'ts):

**Do:**
- `/init` als erstes in jedem neuen Ordner ausführen
- Bullet Points und kurze Überschriften verwenden
- **Hohe Informationsdichte** — komprimiert schreiben
- Wichtigste Regeln **ganz oben** platzieren (Primacy Bias — Anfang wird am besten erinnert)
- Regelmäßig reviewen und ausmisten (wie technische Schulden behandeln)
- Wiederkehrende Fehler als Regel hinzufügen ("Hey, füg das zur CLAUDE.md hinzu")
- Twitter/X für aktuelle Best Practices durchsuchen (Grok fragen)

**Don't:**
- Keine ganzen API-Docs oder Style Guides reinkopieren (zu viele Tokens, Qualität sinkt)
- Keine vagen Anweisungen ("Sei schlau", "Mach keine Fehler")
- Nicht länger als 200–500 Zeilen
- Keinen Voice Dump direkt als CLAUDE.md verwenden (erst verdichten lassen)

### Primacy & Recency Bias:
- Claude erinnert sich gut an den **Anfang** und das **Ende** eines Prompts
- Die **Mitte** wird am schlechtesten erinnert
- → Wichtigste Guardrails immer ganz oben!

### `@include` in CLAUDE.md:
- Mit `@dateiname.md` können andere Dateien eingebunden werden
- Sparsam einsetzen — lieber Rules-Ordner nutzen

### Auto Memory:
- Zusätzlich zur CLAUDE.md wird eine **Memory-Datei** in jede Session injiziert
- Globale Datei — merkt sich Infos über Sessions hinweg
- Beispiel: "Merke dir, dass mein Bruder George heißt" → nächste Session weiß es
- Nicht so wertvoll wie CLAUDE.md, eher "Claudes eigene Notizen"

### Agents (Sub-Agenten):
- Im `.claude/agents/`-Ordner definiert
- Eigene CLAUDE.md-artige Datei pro Agent mit: Tools, Modell, Max Turns, Name, Beschreibung
- **Werden mit eigenem, separatem Kontext gestartet** — das ist der Kernvorteil

**Drei empfohlene Sub-Agenten:**

| Agent | Zweck | Warum eigener Kontext? |
|---|---|---|
| **Research** | Internet-Recherche, Daten sammeln | Verschmutzt nicht den Parent-Kontext. 100k Tokens Recherche → nur 2k Zusammenfassung zurück = 50x günstiger |
| **Reviewer** | Code mit frischen Augen prüfen | Kein Bias vom Schreib-Prozess. Wie ein menschlicher Code-Reviewer |
| **QA/Testing** | Automatisierte Tests ausführen | Hält Test-Ergebnisse vom Haupt-Agenten fern |

- **Research:** Nutzt günstigere Modelle (Sonnet, Haiku) für die Recherche
- **Reviewer:** Profitiert davon, KEINEN Kontext zu haben — sieht den Code objektiv
- **QA:** Erleichtert Test-Driven Development, analog zum Screenshot-Loop bei Design

### Skills (ehem. Custom Slash Commands):
- Im `.claude/skills/`-Ordner definiert
- Unterschied zu Agents: Skills geben Anweisungen an den **Parent-Agenten** (kein separater Agent)
- = Eine Liste von Instruktionen für eine bestimmte Aufgabe

**Beispiel "Shop Amazon":**
- Skill browst Amazon via Chrome DevTools MCP
- Sucht Produkte, vergleicht, präsentiert Optionen
- Kaufentscheidung bleibt beim User (Sicherheits-Stop eingebaut)
- "Wir haben quasi eine API aus Amazon gemacht, die es absichtlich nicht gibt"

**Weitere Skill-Beispiele von Nick:**
- Upwork-Jobs scrapen und bewerben
- Lead-Scraping
- Willkommens-E-Mails an neue Kunden senden
- Deliverables automatisch erstellen

**Skills entwickeln:**
1. Claude bitten, den Skill zu formatieren
2. An frische Claude-Instanz geben, testen
3. Feedback geben, Skill verbessern
4. Iterieren: 70% → 80% → 90% → 98–99% Genauigkeit
- "Die meisten Menschen machen mehr als 1–2% Fehler"

## Kapitel 14–15: Permission Modes (1:31:39)

### Vier Haupt-Modi:

| Modus | Beschreibung | Wann nutzen? |
|---|---|---|
| **Ask before edits** (Default) | Fragt vor jeder Änderung | Hochrisiko-Codebasen, selten genutzt |
| **Edit automatically** | Ändert bestehende Dateien automatisch, fragt bei neuen | Guter Kompromiss |
| **Plan Mode** | Nur lesen + recherchieren, keine Änderungen | Vor komplexen Builds — extrem wertvoll |
| **Bypass Permissions** | Volle Freiheit | Nick's Standard, höchste Produktivität |

### Bypass Permissions — Risiken:
- Ein Fall: Claude hat `sudo rm -rf` ausgeführt und die Festplatte gelöscht
- **Extrem selten**, aber möglich
- Kann auch viele unnötige Dateien erstellen → Workspace-Bloat
- **Tipp:** Regelmäßig Claude bitten, den Workspace aufzuräumen

### Bypass Permissions aktivieren:
- Extensions → Claude Code → Zahnrad → Settings → "Dangerously skip permissions" aktivieren
- Nicht standardmäßig verfügbar

### `/permissions` — Granulare Tool-Kontrolle:
- Einzelne Tools (Bash, Web Fetch etc.) individuell erlauben/sperren
- Nützlich für Team-Settings

### Delegate Mode:
- Für Agent Team Leads — kann nur Aufgaben delegieren, nichts selbst ausführen

## Plan Mode — Deep Dive (1:40:45)

### Was Plan Mode macht:
- **Nur lesen:** Kann Dateien lesen, Internet recherchieren, nachdenken
- **Keine Änderungen** an Dateien
- Erstellt ein detailliertes Plan-Dokument

### Warum Plan Mode so wertvoll ist:

**Ohne Plan:**
- 15 Min bauen → 5 Min testen → Fehler → 15 Min neu bauen → ... = 35+ Min + viele Tokens

**Mit Plan:**
- 5 Min planen → Fehler im Plan erkennen → 5 Min neuen Plan → 5–15 Min bauen = 15–25 Min + weniger Tokens

**"Eine Minute Planung spart 10 Minuten Bauen."**

- Analog zur Bauplanung: Besser den Bauplan ändern als das fertige Gebäude abreißen
- Gilt nicht nur für Claude Code, sondern für jede Art von Projektentwicklung

## Kapitel 16–17: Full-Stack App mit Plan Mode bauen (1:44:33)

### Praxisbeispiel: Proposal Generator (à la PandaDoc)

**Was gebaut wurde:**
- Vollständige Web-App mit Login, Dashboard, KI-generierte Proposals
- E-Signatur-Funktion
- Stripe-Zahlung integriert
- Öffentliche URLs zum Teilen mit Kunden
- Konfetti-Animation nach Zahlung
- Kalender-Link für Kickoff-Call

**Der Prozess:**
1. **Voice Dump** aller Anforderungen in eine Textdatei
2. **Plan Mode** aktivieren → Claude stellt Rückfragen (Framework, DB, Design etc.)
3. Plan-Dokument wird erstellt (Tech Stack, DB Schema, Routes, User Flow)
4. Auf **Bypass Permissions** wechseln
5. API Keys bereitstellen (Supabase, Stripe, Anthropic)
6. Claude baut die App — Nick ging zwischendurch Lachs marinieren
7. Iteratives Feedback per Voice: Spacing, Breiten, Bilder, UX-Verbesserungen
8. **Deployment auf Netlify** — Claude erklärt die Schritte

**Zeitaufwand:** Ca. 10–15 Minuten aktive Arbeit (Rest: Warten + Kochen)

### Key Takeaways:
- **Kein Programmierwissen nötig** — Nick hat nur gesagt, WAS er will, nicht WIE
- Plan Mode hat den Build drastisch beschleunigt und Token-Verbrauch reduziert
- **Parallelisieren:** Während Claude baut, andere Dinge tun (API-Keys besorgen, kochen etc.)
- **GitHub:** Wenn Claude sagt "erstell ein Repo" → einfach Claude bitten, es selbst zu tun
- **Der echte Wert:** Deine Ideen und dein Urteilsvermögen — die technische Umsetzung übernimmt Claude

---

## Kapitel 18: Sicherheitswarnung für Vibe-Coded Apps (2:07:51)

### Context bei 100% — Auto-Komprimierung:
- Wenn Context 99–100% erreicht → automatische Komprimierung aller bisherigen Nachrichten
- Text wird in höhere Informationsdichte umgewandelt
- Mehr Information in weniger Tokens → nächster Prompt ist besser + günstiger

### Sicherheitshinweise für öffentliche Apps:
- **Nicht einfach vibe-coded Apps öffentlich ins Internet stellen und Geld verlangen**
- Claude Code patcht nicht 100% aller Sicherheitslücken (Frontend + Backend)
- Vor Veröffentlichung: Entwickler für Security-Review beauftragen (ein paar hundert Euro)
- Keine offensichtlichen/kurzen URLs verwenden (Scanner durchsuchen ständig das Internet)
- Nick nutzt selbst-gebaute Apps nur **intern** für Teams und Kunden, nicht als öffentliche Produkte
- Warnendes Beispiel: CloudBot → MoltBot → OpenCloud — jede Version hatte Sicherheitslücken, Prompt Injection, Hacks

## Kapitel 19: Context Management erklärt (2:13:54)

### `/context` — Was verbraucht deine Tokens?

Aufschlüsselung eines frischen Claude Code Starts (~26.400 Tokens / 13%):

| Kategorie | Tokens | Beschreibung |
|---|---|---|
| **System Tools** | ~16.800 (8,4%) | Bash, Web Search, Read, Write, Edit, Glob, Grep, Notebook Edit, Web Fetch, Task, Plan Mode etc. — **nicht änderbar** |
| **System Prompt** | ~10.000 | Global CLAUDE.md + lokale CLAUDE.md + Rules |
| **MCP Tools** | variabel (2,8%+) | Selbst installierte Tools (Chrome DevTools, ClickUp etc.) |
| **Memory** | ~88 | MEMORY.md — Claudes Notizen |
| **Skills** | ~60 pro Skill | Nur Front Matter geladen (Name + Beschreibung) — extrem effizient! |
| **Messages** | variabel | Deine tatsächlichen Nachrichten |
| **Free Space** | Rest | Verfügbarer Platz |

### Wichtig zu wissen:
- **All das wird berechnet** — auch die versteckten System-Injections
- Jede neue Session hat einen "Fixkostensockel" von 15.000–45.000 Tokens bevor du überhaupt tippst
- **Thinking-Tab** wird separat berechnet, belegt KEINEN Platz im Context Window
- Thinking wird nach der Antwort "eingeklappt" und verschwindet aus dem Kontext

### Liste aller System-Tools:
Task, Task Output, Bash, Glob, Grep, Read, Edit, Write, Notebook Edit, Web Fetch, Web Search, Todo Write, Ask User Question, Enter/Exit Plan Mode, Skill, Task Stop

## Kapitel 20: MCP Tools im Context (2:20:00)

### MCP vs. System Tools:
- **System Tools** = von Anthropic vorgegeben, nicht änderbar
- **MCP Tools** = von dir selbst installiert, du kontrollierst sie

### Problem: MCP-Bloat
- Schlecht geschriebene MCPs können 20.000+ Tokens verbrauchen
- Ein einzelnes MCP-Tool kann mehr Tokens kosten als ALLE Skills zusammen
- Beispiel: ClickUp MCP Search Tool = 1.600 Tokens vs. Scrape-Leads-Skill = 63 Tokens

### Warum Skills so wenig Tokens brauchen:
- **Nur der Front Matter** (Name, Beschreibung, erlaubte Tools) wird in den Context geladen
- Der eigentliche Skill-Inhalt wird erst geladen, wenn Claude ihn tatsächlich braucht
- → Bessere Entscheidungen am Anfang der Session + weniger Kosten

### Auto Tool Search:
- Wenn MCP-Tool-Beschreibungen > 10% des Context Windows → Claude lädt nicht alle
- Stattdessen: Sucht erst in einer Tool-Liste, lädt nur das benötigte Tool

## Kapitel 21: Strategien für Token-Management (2:27:25)

### Wichtigste Strategien:

1. **`/cost`** regelmäßig checken — Token-Verbrauch im Blick behalten
2. **Status Line** einrichten (nur im Terminal): `/statusline` → z.B. Token-Ladebalken anzeigen
3. **`/compact`** manuell ausführen — komprimiert Konversationshistorie mit optionalen Prioritäts-Anweisungen
4. **`/clear`** bei Themenwechsel — startet frisch ohne alten Kontext
5. **Knapp formulieren** — oder Voice Dump → in günstigerem Modell zusammenfassen → erst dann an Claude senden
6. **Richtige Modellwahl:** Günstigere Modelle (Sonnet, Haiku) für Sub-Agenten
7. **MCP-Overhead reduzieren:** Nur nötige MCPs installieren, besser Skills statt MCPs
8. **Instructions von CLAUDE.md → Skills verschieben:** Skills laden on-demand, CLAUDE.md immer
9. **Extended Thinking nutzen:** Mehr Reasoning-Tokens (separat), weniger Output-Tokens im Context
10. **Spezifische Prompts:** "Fix Feature X in Datei Y" statt "Verbessere die Codebase"
11. **Plan Mode vor dem Bauen:** Spart massiv Tokens bei der eigentlichen Umsetzung

### Auto-Compact Buffer:
- Bei ~33.000 verbleibenden Tokens → automatische Komprimierung
- Auch manuell via `/compact` auslösbar
- Komprimierung = chronologische Zusammenfassung aller bisherigen Nachrichten
- Claude ist gut darin, Wichtiges beizubehalten

### Agent Teams — Token-Warnung:
- Verbrauchen ~7x mehr Tokens als normale Sessions
- Jeder Teammate hat eigenes Context Window
- Nur nutzen, wenn Token-Effizienz nicht Priorität ist

## Kapitel 22–23: Skills erstellen und strukturieren (2:33:42)

### Nicks tägliche Skills (Beispiele):
- **Scrape Leads** — Leads scrapen, verifizieren, klassifizieren, in Google Sheet laden
- **Classify Leads** — LLM-basierte Lead-Klassifizierung
- **Create Proposals** — Automatische Proposal-Generierung
- **Find Outliers** — Nischen-Outliers finden
- **Email Auto-Reply** — E-Mails lesen und beantworten
- **YouTube Edit** — Videos schneiden
- **Client Onboarding** — Neue Kunden onboarden
- **Upwork Apply** — Auf Upwork-Jobs bewerben
- **School Monitor** — School-Posts monitoren und klassifizieren
- **Literature Research** — Wissenschaftliche Recherche (PubMed etc.)

### Skill-Struktur:

```
.claude/skills/
└── skill-name/
    ├── SKILL.md          # Orchestrator — Checklist + Instruktionen
    └── scripts/          # Ausführbare Scripts (Python etc.)
        ├── scrape.py
        ├── classify.py
        └── upload.py
```

### Wie Skills funktionieren (Orchester-Analogie):
- **SKILL.md** = der Dirigent (Orchestrator) — definiert die Reihenfolge
- **Scripts** = die Musiker — führen die einzelnen Aufgaben aus
- Claude nutzt die Scripts wie eigene Tools (analog zu Bash, Web Search etc.)
- **Fehlerbehandlung:** Wenn ein Schritt fehlschlägt, nutzt Claude seine Intelligenz zur Korrektur UND aktualisiert den Skill für die Zukunft

### Praxisbeispiel: Lead Scraping
- 1.000 Leads in 87 Sekunden gescraped (4 parallele Scraper à 250)
- Automatisch in Google Sheet hochgeladen
- E-Mails angereichert
- Fehler bei Upload → Claude hat selbst die API-Doku gelesen und korrigiert
- Vorher: 30+ Minuten manuell → Jetzt: unter 2 Minuten

### Praxisbeispiel: Website-Generator-Skill
- Input: Google Sheet mit Prospect-Daten
- Output: Individuelle Website pro Prospect in ~30 Sekunden
- Bei 10 parallelen Instanzen: ~3 Sekunden pro Website
- 10.000 Websites in ~8 Stunden möglich

### Nicks Business-Impact:
- Über $300k/Monat Gewinn, **keine Mitarbeiter mehr** für diese Aufgaben
- Alles über Skills automatisiert — "warum einen Tag auf einen Contractor warten?"

## Kapitel 24: Neuen Skill erstellen (2:44:39)

### Prozess:
1. **Voice Dump** aller Anforderungen
2. Template/Design-Inspiration beifügen (Screenshot + HTML/CSS)
3. Beispiel-Input-Daten mitgeben (z.B. Google Sheet)
4. Claude erstellt den Skill (fragt ggf. Rückfragen)
5. Claude aktiviert Plan Mode automatisch bei komplexeren Builds (bei Bypass Permissions)
6. Testen → Feedback → Iterieren

## Kapitel 25: Model Context Protocol (MCP) (2:51:02)

### Was ist MCP?
- **"Skills, die andere Leute für dich gemacht haben"**
- Gibt Claude Zugriff auf externe Software/Services
- Funktioniert wie eigene Tools (Web Search, Bash etc.), aber von Dritten entwickelt

### Wo findet man MCPs?
- mcpservers.org
- modelcontextprotocol/servers (GitHub)
- mcpmarket
- Oder: "[Tool-Name] MCP server" googeln

### Installation:
1. JSON-Snippet von der MCP-Seite kopieren
2. In Claude Code einfügen: "Install this in my local workspace"
3. Ggf. API-Key bereitstellen
4. Claude Code Session neu starten

### Nicks Lieblings-MCP: Chrome DevTools
- Steuert einen echten Chrome-Browser
- Screenshots, Navigation, Klicks, Formulare ausfüllen
- "100x schneller als die eingebauten Browser-Tools"
- Nutzt er täglich, mehrmals

### Praxisbeispiel: ClickUp MCP
- MCP installiert → API-Key eingegeben
- "Create a new content idea called Claude Code course"
- Claude durchsucht alle Listen, erstellt Task im richtigen Board
- Status geändert — alles in Sekunden

## Kapitel 26: MCP vs. Skills — Token-Vergleich (2:58:15)

### Das Token-Problem bei MCPs:

| | MCP | Skill |
|---|---|---|
| **Token-Verbrauch** | ~20.000 (alle Tools geladen) | ~60 (nur Front Matter) |
| **Setup-Zeit** | 2 Minuten | 5+ Minuten |
| **Geschwindigkeit** | Langsamer (MCP-Overhead) | Schneller (direkte API-Calls) |
| **Flexibilität** | Vorgegeben | Voll anpassbar |

### Nicks Workflow: MCP → Skill
1. **MCP installieren** zum schnellen Testen: "Kann Claude X, Y, Z mit diesem Tool?"
2. Wenn ja → **Skill daraus bauen** mit direkten API-Calls
3. MCP wieder entfernen → Token-Ersparnis

### Praxisbeispiel: Gmail-Labels
- **Mit MCP:** Langsam, hoher Token-Verbrauch
- **Als Skill:** 100 E-Mails in 36 Sekunden klassifiziert (0,36 Sek/E-Mail)
- 5–10x schneller als MCP-Version

## Kapitel 27–28: Plugins (3:07:58)

### Claude Code Plugins:
- Zusätzliche Erweiterungen über "Customize and manage plugins"
- **Nicht essentiell** — Vanilla Claude Code funktioniert sehr gut ohne Plugins
- Nick nutzt kaum Plugins, erwartet dass sie in Skills aufgehen werden

### Erwähnenswerte Plugins:
- **cloud-mem** — speichert alle Nachrichten in Memory-Datei, durchsuchbar über Sessions
- **Front-end Design** (Anthropic) — soll Design-Qualität verbessern, Nick findet Screenshot-Workflow besser
- **Context7** — durchsucht API-Docs token-effizient, komprimiert Dokumentation automatisch

### Plugin-Quellen:
- Claude Code Plugins Directory (offiziell von Anthropic)
- Claude Code Marketplace (Third-Party)
- Installation: Straightforward, ähnlich wie MCP

## Kapitel 29–31: Sub-Agenten Deep Dive (3:11:13)

### Realistische Einschätzung:
- Sub-Agenten sind **kein Allheilmittel** — alles geht auch mit einem einzelnen Agent
- Hauptvorteil: **Parallelisierung** und **günstigere Modelle** für Teilaufgaben
- Verbrauchen viele Tokens, können teuer werden

### Praxisbeispiel: Gmail-Labels parallelisieren
- Skill → Sub-Agent umgewandelt: 10 parallele Classifier
- **100 E-Mails:** 36 Sek (seriell) → 30 Sek (parallel) — nur 6 Sek gespart bei kleiner Menge
- **1.000 E-Mails:** ~1 Minute statt ~6 Minuten — hier zeigt sich der Vorteil
- Problem: Sub-Agenten können zu viel Text zurückgeben → Parent-Context überlaufen → Lösung: nur Labels zurückgeben, nicht den E-Mail-Text

### Wahrscheinlichkeits-Mathematik bei Sub-Agenten:
- Bei 95% Erfolgsrate pro Agent: 3 Agents = 85,7% | 10 Agents = 59% | 50 Agents = 7%
- → **Aufgaben so einfach wie möglich halten** für Sub-Agenten
- Nicht alles parallelisieren — nur wo es Sinn macht

### Die drei nützlichsten Sub-Agenten:

| Agent | Funktion | Modell-Empfehlung |
|---|---|---|
| **Code Reviewer** | Code objektiv prüfen (ohne Bias des Schreibers) | Sonnet |
| **Researcher** | Parallele Recherche, spezifische Quellen | Sonnet |
| **QA/Tester** | Tests generieren und ausführen | Sonnet |

### Empfohlener Workflow: Write → Review → QA → Ship
1. Parent Agent schreibt Code
2. Code Reviewer Sub-Agent prüft (parallel mit QA)
3. QA Sub-Agent generiert und führt Tests aus
4. Parent Agent integriert Feedback und fixt Issues

## Kapitel 33–34: Agent Teams (3:26:29)

### Was sind Agent Teams?
- **Fortgeschrittenere Version von Sub-Agenten**
- Ein "Team Lead" Agent orchestriert mehrere Teammate-Agents
- Teammates sind **volle Claude Code Instanzen** (eigene CLAUDE.md, MCPs, Skills)
- Können **untereinander kommunizieren** (nicht nur mit dem Team Lead)

### Agent Teams vs. Sub-Agenten:

| | Sub-Agenten | Agent Teams |
|---|---|---|
| Context | Nur vom Parent übergeben | Eigenes volles Context Window |
| Kommunikation | Nur mit Parent | Untereinander + mit Team Lead |
| Koordination | Parent managed alles | Shared Task List, Self-Coordination |
| Kosten | Relativ günstig | **~7x teurer** (jeder Teammate = eigene Claude-Instanz) |
| Unabhängigkeit | Begrenzt | Voll unabhängig |
| Best für | Fokussierte Einzelaufgaben | Komplexe Arbeit mit Diskussion/Zusammenarbeit |

### Aktivierung:
- Standardmäßig deaktiviert (experimentelles Feature)
- In `settings.json`: `{"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}}`

### Bedienung:
- Terminal: `Shift+Up/Down` zum Wechseln zwischen Agents
- Jeder Agent zeigt eigene Token-Nutzung
- Team Lead wartet auf alle Agents, fasst Ergebnisse zusammen
- Idle-Agents werden nach Timeout heruntergefahren

### Praxisbeispiel 1: Drei Website-Designs parallel
- Team Lead recherchiert erst über Nick, dann spawnt 3 Design-Agents
- Ergebnis: 3 fundamental verschiedene Websites in ~2 Minuten
- Gewinner-Design → 3 weitere Iterationen mit Research-Agents (Design-Prinzipien, Copywriting, Beispiel-Sites)
- Inspiriert von Ali Abdaal, Hormozi, Dan Koe, Justin Welsh

### Praxisbeispiel 2: Open-Source Security Audit
- 10 Scanner-Agents lesen parallell die gesamte Codebase
- 4 Dokumentations-Agents + 2 Debate-Agents (Devil's Advocate)
- Debate-Agents argumentieren adversarial: "Ist das ein echtes Problem?" vs. "Ja, das muss gefixt werden"
- 15 Security-Issues gefunden → 15 Fixer-Agents geplant
- **Kosten: ~$80 für ~15 Minuten** — ersetzt mehrere Wochen Entwickler-Arbeit
- 1,3 Mio. Tokens verbraucht

### Wichtige Warnungen:
- **"Nuklearwaffe für dein Wallet"** — Kosten können schnell explodieren
- Tokens sind nicht erstattbar
- Immer Limits setzen
- Nicht für jede Aufgabe sinnvoll — oft reicht ein einzelner Agent

## Kapitel 35: Git Worktrees (3:56:08)

### Was sind Git Worktrees?
- Mehrere Agents arbeiten auf **separaten Git-Branches** gleichzeitig
- Jeder Branch = eigener Ordner = keine Dateikonflikte
- Am Ende: Merge zurück in den Main-Branch

### Warum Worktrees?
- **Eliminiert Agent-Konflikte:** Zwei Agents können nicht dieselbe Datei gleichzeitig ändern
- Saubere Trennung: Feature A in Branch A, Feature B in Branch B
- Merge-Schritt am Ende vereint alles

### Praxisbeispiel:
- Hauptseite (index.html) → 3 Worktrees für About, Contact, Services
- 3 Agents arbeiten parallel auf eigenen Branches
- Jeder erstellt seine Seite unabhängig
- Merge am Ende vereint alle neuen Seiten

### Wann Worktrees vs. Agent Teams?
- Worktrees = extra Sicherheitsschicht gegen Dateikonflikte
- Können mit Agent Teams kombiniert werden
- Besonders nützlich bei größeren Codebasen

## Kapitel 36: Deployment mit Modal (4:03:09)

### Was ist Modal?
- Service zum Deployen von Backend-Funktionen und APIs
- Extrem günstig (~$0.50 Verbrauch über Monate bei regelmäßiger Nutzung)
- $5 Gratis-Credits beim Start (bis $30 mit Onboarding-Tasks)
- Günstiger als Make.com, N8N, Zapier für viele Use Cases

### Wie es funktioniert:
1. Account erstellen auf modal.com
2. API Token generieren
3. Claude Code das Token geben
4. "Deploy X as API endpoint" sagen → öffentliche URL in Sekunden

### Praxisbeispiel: Skill als Web-Service
- Scrape-Leads Skill → als URL deployed
- Formular fragt: Was scrapen? Wo? Wie viele?
- Ergebnis: CSV-Download mit allen Leads
- Alles in unter 2 Minuten aufgesetzt

### Einsatzmöglichkeiten:
- Websites und Web-Apps öffentlich machen
- Eigene API-Endpoints für Webhooks
- Integration mit No-Code Tools (Make.com, N8N, Zapier, Lindy)
- Interne Tools als Web-Service bereitstellen
- Ad-Campaign Tracking, Marketing-Automationen

## Zusammenfassung: Nicks Empfehlungen

### Die 80/20-Regel für Claude Code:
1. **CLAUDE.md** gut pflegen (200–500 Zeilen, hohe Informationsdichte)
2. **Plan Mode** vor jedem komplexen Build
3. **Skills** für wiederkehrende Aufgaben (token-effizient, on-demand)
4. **Sub-Agenten** für Research, Review, QA (günstigere Modelle)
5. **Agent Teams** nur bei wirklich komplexen, parallelisierbaren Aufgaben
6. **MCP** zum schnellen Testen → dann in Skill umwandeln
7. **Git Worktrees** bei Multi-Agent Codebase-Arbeit
8. **Modal** für schnelles Deployment

### Kern-Philosophie (durchgängig):
- **Task → Do → Verify** — immer Verifikationsloop einbauen
- **Plan zuerst** — 1 Minute Planung spart 10 Minuten Bauen
- **Kein Programmierwissen nötig** — Ideen und Urteilsvermögen sind der Wert
- **KI = Geschwindigkeit beim Iterieren**, nicht Perfektion beim ersten Versuch
- **Geld = Zeit:** Tokens gezielt in Zeitersparnis umwandeln

---

*Quelle: Nick Saraev, YouTube Tutorial "Claude Code for Beginners"*
*Video: https://youtu.be/QoQBzR1NIqI (ca. 4:10 Stunden)*
*Alle 36 Kapitel vollständig zusammengefasst: 2026-03-27*
