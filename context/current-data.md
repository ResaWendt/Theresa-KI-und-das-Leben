# Aktuelle Daten

## Leitplanken

| Parameter | Wert |
|---|---|
| Max. Arbeitszeit | 20 Stunden/Woche |
| Min. Umsatz (netto) | 15.000€/Monat |
| Ziel Umsatz (netto) | 20.000€/Monat |

## Aktueller Stand

- **Phase:** Aufbau — noch keine Kundengespräche
- **LinkedIn:** Profil weitgehend umgesetzt (2026-03-11): Banner, Headline, Info/Über mich, Berufserfahrung, Skills, Ausbildung, Sprachen sind live. Offen: Custom URL, Creator Mode, Featured Section. KIPA-Recap-Post veröffentlicht (2026-03-10). Post "Neuanfang" Entwurf 2, noch nicht final. Posting-Rhythmus: Mittwoch, 8:30 Uhr.
- **Positionierung:** Primär Reiseveranstalter, untergeordnet inhabergeführte Unternehmen allgemein. Mitgründerin von "Wir sind reisen" (wirsindreisen.at) als Credibility.
- **Workshop-Insights:** Aufgelöst und verteilt nach `reference/` (positionierung.md, social-media.md, produktentwicklung.md). Leitplanken in eigener Datei `context/leitplanken.md` (5 Leitplanken inkl. Strategielose Authentizität).
- **Automatisierungen:** Trainerabrechnung fertig. Offen: Vermögensübersicht, Chatbot UFC-Wien.
- **UFC-Turnier:** n8n-Workflow gebaut + getestet (Webhook → Google Sheets). Vercel offline, Workflow deaktiviert — Security-Härtung vor Re-Deploy nötig.
- **Akquise-Ansatz:** Potentialanalyse pitchen — vor dem Erstgespräch KI-Anwendungsfälle für die Branche recherchieren, dann konkret zeigen wo der Hebel liegt
- **Website:** TODO — Onepager mit Heldenreise, um Kunden zu pitchen
- **Angebotspakete:** Noch nicht entwickelt (kommt nach ersten Beratungen)
- **Multiplikatoren:** Noch nicht kontaktiert
- **Kunden:** 0
- **Umsatz:** 0

## TODOs nach Priorität

> Wird bei jedem `/prime` ausgegeben und bei jedem `/shutdown` aktualisiert.

### PRIO 1 — Sofort / Diese Woche

| # | TODO | Bereich | Deadline | Status |
|---|---|---|---|---|
| 1.1 | Schulung Michaela Nachbereitung: Feedback einholen, Materialien ggf. anpassen, Follow-up GPTs anbieten | KI-Projekt | nächste Session | Schulung war 20.03.2026, Prompting-Anleitungen (3 HTMLs) erstellt |
| 1.3 | LinkedIn-Post "Neuanfang" finalisieren und veröffentlichen | LinkedIn | diese Woche | Entwurf 2 |
| 1.4 | LinkedIn-Profil vervollständigen: Custom URL, Creator Mode, Featured Section | LinkedIn | diese Woche | offen (Berufserfahrung, Skills, Ausbildung, Sprachen erledigt) |
| 1.5 | LinkedIn: Reiseveranstalter identifizieren, vernetzen, Ansprache mit Förderungs-Pitch | Akquise | laufend | offen |
| 1.6 | Wöchentlicher LinkedIn-Post: **Mittwoch, 8:30 Uhr** | LinkedIn | laufend | festgelegt |
| 1.7 | LinkedIn-Post "KI ist mein Turbo. Aber nicht mein Gehirn. Und schon gar nicht mein Herz." ausarbeiten | LinkedIn | Mi 26.03. | Thema festgelegt, Beispiel noch offen |
| 1.8 | Prompting-Anleitungen reviewen: 3 HTMLs (Self Evaluation, Newsletter, LinkedIn) + Anwendungen Automatisierung/Klassifizierung besprechen | Schulung | nächste Session | erstellt, Review offen |
| 1.11 | UFC-Turnier: Security-Maßnahmen umsetzen, dann Vercel re-deploy + n8n-Workflow aktivieren | KI-Projekt | nächste Session | Workflow gebaut + getestet, aktuell offline/deaktiviert, 7 Security-Maßnahmen offen |

### PRIO 2 — Kurzfristig (März/April)

| # | TODO | Bereich | Status |
|---|---|---|---|
| 2.1 | Gewerbe-Erkundigungen: Unternehmensberatung anmelden, SVS-Ausnahme, Firmenwortlaut | Gewerbe | offen |
| 2.2 | Gewerbe-Erkundigungen: Wechsel auf Lehre & Training prüfen | Gewerbe | offen |
| 2.3 | Gewerbe-Erkundigungen: Zweites Gewerbe IT-Umsetzung prüfen | Gewerbe | offen |
| 2.4 | Business Development Phasenplan: Aufbau → erste Kunden → Standardisierung mit Meilensteinen | Strategie | offen |
| 2.6 | Content-Wissensbasis aufbauen (Copywriting, Storytelling, Hooks) | Content | offen |
| 2.7 | KMU.DIGITAL Beraterzertifizierung: Voraussetzungen prüfen, Hearing anstreben | Akquise | offen |

### PRIO 3 — Laufend / Untergeordnet

| # | TODO | Bereich | Status |
|---|---|---|---|
| 3.1 | Automatisierung fertigstellen: Vermögensübersicht | Automatisierung | angefangen |
| 3.2 | Social Media Automatisierung: Partyfechten + UFC Wien | KI-Projekt | offen |
| 3.3 | ChatBot für UFC Wien: Anforderungen, Technologie, Prototyp | KI-Projekt | offen |
| 3.5 | KIPA-Anregung an Garrit: Positionierung/Mindset erweitern auf EiS | KIPA | offen |
| 3.6 | System-Wartung: Linux, n8n — monatlich | Wartung | laufend, letzte Wartung 2026-03-28 |

### PRIO 4 — Claude Code Workspace Optimierung

> Abgeleitet aus Nick Saraev Tutorial (reference/claude-code-tutorial-nick-saraev.md), 2026-03-27

| # | TODO | Bereich | Priorität | Status |
|---|---|---|---|---|
| 4.1 | Verifikations-Loop in Workflows einbauen (Self-Review-Schritt in /implement für HTML-Outputs) | Workspace | hoch | offen |
| 4.2 | Voice-Input direkt in Claude Code testen (Spracheingabe statt Tippen) | Workspace | hoch | offen |
| 4.3 | Chrome DevTools MCP installieren (Browser steuern, Screenshots, Daten sammeln) | Workspace | hoch | offen |
| 4.4 | Research Sub-Agent anlegen (.claude/agents/) — günstigeres Modell für breite Recherchen | Workspace | mittel | offen |
| 4.5 | Globale CLAUDE.md anlegen (~/.claude/CLAUDE.md) — Sprache, Kommunikationsstil, workspace-übergreifende Regeln | Workspace | mittel | offen |
| 4.6 | Netlify/Modal für Deployment einrichten (Onepager, Kunden-Tools) | Workspace | mittel | offen |
| 4.7 | Status Line einrichten (Token-Verbrauch im Terminal sichtbar) | Workspace | niedrig | offen |
| 4.8 | Agent Teams evaluieren (experimentell, erst bei großen parallelen Projekten) | Workspace | niedrig | offen |

### Geplante KI-Projekte

> Übersicht aller KI-bezogenen Projekte — eigene und für Kunden/Partner.

| # | Projekt | Beschreibung | Status |
|---|---|---|---|
| KI-1 | Schulung Prompting Michaela | Mini-Einschulung Prompting (siehe 1.1) | Schulung durchgeführt 20.03.2026, 3 Prompting-Anleitungen als HTML erstellt, Nachbereitung offen |
| KI-2 | Website Onepager | Onepager mit Heldenreise konzipieren (ehem. 2.7) | offen |
| KI-3 | Trainerabrechnung | Automatisierung der Abrechnung | **fertig** |
| KI-4 | Vermögensübersicht | Automatisierte Aktualisierung | angefangen |
| KI-5 | Social Media Automatisierung PF + UFC Wien | Content-Planung und -Erstellung automatisieren | offen |
| KI-6 | ChatBot UFC Wien | Anforderungen, Technologie, Prototyp | offen |
| KI-7 | Mitgliedsanträge UFC Wien | Automatisierung: Anträge auf Mitgliedschaft → Übertrag in Excel-Tabelle | offen |
| KI-9 | Turnieranmeldung UFC Wien | HTML-Formular → n8n Webhook → Google Sheets | Workflow gebaut + getestet, aktuell offline, Security-Härtung offen |
| KI-8 | KI-News Daily | Tägliche KI-News automatisiert, priorisiert nach Theresas Bedürfnissen/Interessen | offen |

### Erledigt

- [x] LinkedIn-Texte erstellen (erledigt)
- [x] LinkedIn-Profil Kerndaten umsetzen: Banner, Headline, Info/Über mich (2026-03-10)
- [x] KIPA-Recap-Post veröffentlichen (2026-03-10)
- [x] Business-Plan erstellen (2026-03-10, siehe `outputs/business-plan.md`)
- [x] LinkedIn-Profil: Berufserfahrung, Skills, Ausbildung, Sprachen umgesetzt (2026-03-11)
- [x] Posting-Rhythmus festgelegt: Mittwoch, 8:30 Uhr (2026-03-11)
- [x] Post-Ideen Pipeline aufgelöst und verteilt (2026-03-11)
- [x] Workshop-Insights aufgelöst → `reference/` + `context/leitplanken.md` (2026-03-11)
- [x] Leitplanke "Strategielose Authentizität" ergänzt (2026-03-11)
- [x] Akquise-Strategien in Business-Plan ergänzt: Testkunden + Potentialanalyse (2026-03-11)
- [x] KI-Förderungen Österreich recherchiert → `reference/ki-foerderungen-oesterreich.md` (2026-03-12)
- [x] KI-Projekte Übersicht angelegt in current-data.md (2026-03-12)
- [x] Nächster LinkedIn-Post thematisch festgelegt: "KI ist mein Turbo. Aber nicht mein Gehirn. Und schon gar nicht mein Herz." (2026-03-12)
- [x] Schulungskonzept Michaela: HTML-Präsentation erstellt (32 Slides, Dark Theme, personalisiert auf Michaela) — IN ARBEIT, Feinschliff nächste Session (2026-03-18)
- [x] Recherche: Aktuelle LLM-Architektur 2026 (GPT-5.4, Claude Opus 4.6, Context Windows 1M, Sora 2) für Schulungsinhalte verifiziert (2026-03-18)
- [x] Recherche: Best Practices Schulungspräsentationen (Slide-Design, 20/80 Theorie/Praxis, Interaktionspunkte) (2026-03-18)
- [x] Michaela-Profil dokumentiert: Senior Account Managerin, Handwerk/Garten/Landwirtschaft, nutzt ChatGPT + Sora (2026-03-18)
- [x] KIPA-Obsidian-Notizen: Alle 27 Bilder aus 9 Notizen ausgelesen und Inhalte dokumentiert (2026-03-19)
- [x] Schulungspräsentation überarbeitet: 36 Slides, KIPA-Slide-Inhalte als CSS-Diagramme eingearbeitet (Glockenkurve, Säulen, Flowcharts, Prompt Dev Zyklus, Praktikant vs. Mitarbeiter) (2026-03-19)
- [x] Neuer Slide "Trainieren vs. Merken": ChatGPT Memory-System recherchiert und korrekt dargestellt (2026-03-19)
- [x] Neuer Slide "Was heute noch dazukommt": Deep Research, Canvas, Sora, KI-Agenten (2026-03-19)
- [x] Sora-Status verifiziert: Noch NICHT in ChatGPT integriert, nur angekündigt — Präsentation + Konzept korrigiert (2026-03-19)
- [x] Grafik "Wie KI-Modelle Fragen beantworten": Clean Rebuild der KIPA-Überblicksgrafik als SVG in Brandfarben, mit PNG-Export (2026-03-19)
- [x] Schulungskonzept aktualisiert: Trainieren vs. Merken, Deep Research, Canvas, Sora, Agenten eingearbeitet (2026-03-19)
- [x] Obsidian-KIPA-Notizen-Pfade in Memory gespeichert für zukünftige Sessions (2026-03-19)
- [x] Schulung Michaela durchgeführt (2026-03-20)
- [x] Prompting-Anleitung: Self Evaluation Prompting als HTML erstellt (2026-03-20)
- [x] Prompting-Anleitung: Newsletter Prompt-Kette mit Self Evaluation als HTML erstellt (2026-03-20)
- [x] Prompting-Anleitung: LinkedIn-Post Prompt-Kette (7 Schritte, AIDA) als HTML erstellt (2026-03-20)
- [x] Nick Saraev Claude Code Tutorial: Vollständiges Transkript (36 Kapitel, 4:10h) auf Deutsch zusammengefasst → `reference/claude-code-tutorial-nick-saraev.md` (2026-03-27)
- [x] Workspace-Vergleich: Nicks Empfehlungen vs. unser Setup — Prioritätenliste erstellt (8 Punkte, PRIO 4 in TODOs) (2026-03-27)
- [x] n8n MCP Server Security Assessment: GitHub-Repo analysiert, DISABLED_TOOLS Einschränkung dokumentiert (2026-03-27)
- [x] Memory: Rules-Ordner-Trigger gespeichert (bei CLAUDE.md > 500 Zeilen aufmerksam machen) (2026-03-27)
- [x] Windows→Linux Migration: settings.local.json bereinigt, transcribe_audio.py ffmpeg-Pfad korrigiert, current-data.md aktualisiert (2026-03-28)
- [x] .gitignore angelegt: .mcp.json, .env, settings.local.json geschützt (2026-03-28)
- [x] n8n MCP Server installiert: .mcp.json konfiguriert, Member-Rolle + Permissions-Modus als Sicherheitskonzept (2026-03-28)
- [x] Vercel CLI installiert (v50.37.3) + Account eingeloggt (2026-03-28)
- [x] n8n MCP Konfiguration global verschoben (lokale .mcp.json → ~/.claude/settings.json), Workshop-Readiness bestätigt (2026-03-28)
- [x] n8n MCP Konfiguration bereinigt: enabledMcpjsonServers-Referenz auf gelöschte .mcp.json entfernt, Permissions vereinfacht (Wildcards), API-Key aus Permissions entfernt (2026-03-28)
- [x] UFC Wien Turnieranmeldung: HTML-Formular erstellt (Multi-Slide, Validierung, Altersklassen-Automatik, Degen/Florett, 15€ Startgeld) (2026-03-28)
- [x] .DS_Store und __pycache__ aus heruntergeladenen Ordnern bereinigt (2026-03-28)
- [x] n8n MCP env-Variablen-Bug gefixt: Wrapper-Skript erstellt, API-Keys in .env ausgelagert (2026-03-28)
- [x] n8n MCP Server global neu installiert: npx→global install, Wrapper-Skript optimiert (stderr→/dev/null), MCP-Tools noch nicht in CC-Session geladen (2026-03-28)
- [x] n8n MCP Root-Cause gefunden: MCP-Server müssen via `claude mcp add` registriert werden (→ ~/.claude.json), nicht manuell in ~/.claude/settings.json. Server jetzt ✓ Connected (2026-03-28)
- [x] Alte MCP-Konfiguration aus ~/.claude/settings.json bereinigt (2026-03-28)
- [x] .DS_Store und __pycache__ erneut bereinigt (Nick Saraev Ordner, umfangreich) (2026-03-28)
- [x] UFC-Turnier n8n-Workflow gebaut + getestet: Webhook → Set → Google Sheets → Respond (2026-03-28)
- [x] UFC-Turnier auf Vercel deployed + getestet, dann wieder offline genommen (Security-Härtung offen) (2026-03-28)
- [x] CC Workshop Garrit (28.03.) teilgenommen (2026-03-28)
- [x] Workspace aufgeräumt: outputs/ in Unterordner (linkedin/, prompt-schulung/, ufc-wien/), assets/ neu, Binärdateien aus reference/ verschoben (2026-03-28)
- [x] Trainerabrechnung fertiggestellt (2026-03-28)
- [x] Heruntergeladene Ordner eingeordnet (Nick Saraev, Prompt Engineering, KI Modelle) (2026-03-28)

### Meilensteine (mittelfristig)

1. Erste Beratungsgespräche geführt
2. Erste zahlende Kunden
3. Angebotspakete definiert
4. 15–20k netto/Monat bei max. 20h/Woche
