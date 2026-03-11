# CLAUDE.md

Diese Datei gibt Claude Code (claude.ai/code) Anweisungen für die Arbeit in diesem Repository.

---

## Was das hier ist

Dies ist der **Workspace von Theresa Wendt** — Inhaberin von Intellenz Development, Prozess- & KI-Beraterin für inhabergeführte Unternehmen. Positionierung: Business-Problemlöserin, die KI als Turbo nutzt. Baut aktuell die Personenmarke "Theresa, KI und das Leben!" auf LinkedIn auf.

Die Umgebung ist für die Arbeit mit Claude Code als Agenten-Assistenten über mehrere Sessions hinweg konzipiert. `/prime` zu Beginn jeder Session laden.

**Diese Datei (CLAUDE.md) ist das Fundament.** Sie wird automatisch am Anfang jeder Session geladen. Halte sie aktuell — sie ist die Single Source of Truth dafür, wie Claude diesen Workspace verstehen und darin arbeiten soll.

---

## Die Claude-User-Beziehung

Claude arbeitet als **Agenten-Assistent** mit Zugriff auf die Workspace-Ordner, Kontext-Dateien, Commands und Outputs. Die Beziehung ist:

- **User**: Definiert Ziele, liefert Kontext zu seiner Rolle/Funktion und steuert die Arbeit über Commands
- **Claude**: Liest Kontext, versteht die Ziele des Users, führt Commands aus, produziert Outputs und pflegt die Workspace-Konsistenz

Claude sollte sich immer über `/prime` am Session-Start orientieren, dann mit vollem Bewusstsein dafür handeln, wer der User ist, was er erreichen möchte und wie dieser Workspace das unterstützt.

---

## Workspace-Struktur

```
.
├── CLAUDE.md              # Diese Datei — Kern-Kontext, immer geladen
├── .claude/
│   └── commands/          # Slash-Commands, die Claude ausführen kann
│       ├── prime.md       # /prime — Session-Initialisierung
│       ├── create-plan.md  # /create-plan — Implementierungspläne erstellen
│       └── implement.md   # /implement — Pläne umsetzen
├── context/               # Hintergrund-Kontext über Theresa und das Business
│   ├── personal-info.md   # Persönlichkeit, Werdegang, Fähigkeiten, Sprache
│   ├── business-info.md   # Intellenz Development, Zielgruppen, Angebote
│   ├── strategy.md        # Strategische Prioritäten und Erfolgskriterien
│   ├── current-data.md    # Aktueller Stand, Meilensteine, Kennzahlen
│   └── leitplanken.md      # Persönliche Leitplanken für Business, Positionierung und Content
├── plans/                 # Implementierungspläne erstellt von /create-plan
├── outputs/               # Arbeitsergebnisse und Deliverables
│   ├── linkedin-profil.md              # LinkedIn-Profiltexte + Banner-Anleitung + Checkliste (in Überarbeitung)
│   ├── linkedin-content-strategie.md   # Content-Strategie "Theresa, KI und das Leben!"
│   ├── linkedin-post-01-neuanfang.md   # LinkedIn-Post "Neuanfang" (Entwurf)
│   ├── linkedin-post-02-kipa-recap.md  # LinkedIn-Post KIPA Recap (FINAL)
│   └── business-plan.md               # Business-Plan & TODOs
├── reference/             # Vorlagen, Beispiele, wiederverwendbare Patterns
│   ├── shell-aliases.md       # Shell-Aliase für Claude Code Start (cs/cr)
│   ├── video-tools.md         # Video-Erstellungstools (Higgsfield, Kling, ElevenLabs etc.)
│   ├── positionierung.md      # Adrian Kraft: Echtheit, Kernkompetenz, KI im Mittelstand
│   ├── social-media.md        # Marco Bednarz: Content-Strategie, Wiederverwertung, Customer Journey
│   └── produktentwicklung.md  # Sophie Schenk: Wert x Preis, Touchpoints, Sichtbarkeit
└── scripts/               # Automatisierungsskripte (Trainerabrechnung, Vermögensübersicht, Chatbot UFC-Wien)
```

**Verzeichnisse:**

| Verzeichnis  | Zweck                                                                                   |
| ------------ | --------------------------------------------------------------------------------------- |
| `context/`   | Wer der User ist, seine Rolle, aktuelle Prioritäten, Strategien. Gelesen von `/prime`. |
| `plans/`     | Detaillierte Implementierungspläne. Erstellt mit `/create-plan`, umgesetzt mit `/implement`. |
| `outputs/`   | Deliverables, Analysen, Reports und Arbeitsergebnisse.                                 |
| `reference/` | Hilfreiche Dokumentation, Vorlagen und Patterns für verschiedene Workflows.            |
| `scripts/`   | Automatisierungsskripte (Trainerabrechnung, Vermögensübersicht, Chatbot UFC-Wien).     |

---

## Commands

### /prime

**Zweck:** Neue Session mit vollem Kontext-Bewusstsein initialisieren.

Am Anfang jeder Session ausführen. Claude wird:

1. CLAUDE.md und Kontext-Dateien lesen
2. Verständnis von User, Workspace und Zielen zusammenfassen
3. Bereitschaft zur Unterstützung bestätigen

### /create-plan [anforderung]

**Zweck:** Detaillierten Implementierungsplan erstellen, bevor Änderungen gemacht werden.

Verwenden beim Hinzufügen neuer Funktionalität, Commands, Skripte oder bei strukturellen Änderungen. Erzeugt ein gründliches Plan-Dokument in `plans/`, das Kontext, Begründung und schrittweise Aufgaben erfasst.

Beispiel: `/create-plan Wettbewerbs-Analyse-Command hinzufügen`

### /implement [plan-pfad]

**Zweck:** Einen mit /create-plan erstellten Plan umsetzen.

Liest den Plan, führt jeden Schritt der Reihe nach aus, validiert die Arbeit und aktualisiert den Plan-Status.

Beispiel: `/implement plans/2026-01-28-wettbewerbs-analyse-command.md`

### /shutdown

**Zweck:** Session sauber beenden.

Workspace scannen, aufräumen, CLAUDE.md und Context-Dateien aktualisieren, committen und pushen. Liefert eine Zusammenfassung der Session.

---

## Aktuelle Outputs

| Datei | Inhalt | Stand |
|---|---|---|
| `outputs/linkedin-profil.md` | LinkedIn-Profiltexte: Banner, Headline, Info/Über mich (alle UMGESETZT), Berufserfahrung, Skills, Ausbildung, Sprachen (UMGESETZT), Checkliste | 2026-03-11 |
| `outputs/linkedin-content-strategie.md` | Content-Strategie "Theresa, KI und das Leben!": 5 Säulen, 25+2 Post-Ideen, Tonalität-Guide, 4-Wochen-Startplan, Engagement-Strategie, Post-Ideen Pipeline | 2026-03-11 |
| `outputs/linkedin-post-01-neuanfang.md` | LinkedIn-Post "Ende 40. Neuanfang." (Säule "Der Weg") — Entwurf 2, noch nicht final | 2026-02-28 |
| `outputs/linkedin-post-02-kipa-recap.md` | LinkedIn-Post KIPA Live-Event Recap Berlin — FINAL, veröffentlicht | 2026-03-10 |
| `outputs/linkedin-post-03-perfekter-tag.md` | LinkedIn-Post "Mein perfekter Tag" (Visionsarbeit, Genius Zone, Kinder/Jugendliche) — FINAL | 2026-03-10 |
| `outputs/business-plan.md` | Business-Plan & TODOs: Prio 1–2, Akquise-Strategien, KI-Projekte, KIPA-Feedback, System-Wartung | 2026-03-11 |

---

## Kritische Anweisung: Diese Datei pflegen

**Wann immer Claude Änderungen am Workspace macht, MUSS Claude prüfen, ob CLAUDE.md aktualisiert werden muss.**

Nach jeder Änderung — ob Commands, Skripte, Workflows oder Strukturänderungen — frage:

1. Fügt diese Änderung neue Funktionalität hinzu, die Benutzer kennen müssen?
2. Ändert sie die oben dokumentierte Workspace-Struktur?
3. Sollte ein neuer Command aufgelistet werden?
4. Braucht context/ neue Dateien dafür?

Falls ja, aktualisiere die entsprechenden Abschnitte. Diese Datei muss immer den aktuellen Zustand des Workspace widerspiegeln, damit zukünftige Sessions genauen Kontext haben.

**Beispiele für Änderungen, die CLAUDE.md-Updates erfordern:**

- Neuen Slash-Command hinzufügen → im Commands-Abschnitt ergänzen
- Neuen Output-Typ erstellen → in Workspace-Struktur dokumentieren oder Abschnitt erstellen
- Skript hinzufügen → Zweck und Verwendung dokumentieren
- Workflow-Patterns ändern → entsprechende Dokumentation aktualisieren

---

## Für Benutzer, die dieses Template herunterladen

Um diesen Workspace an deine eigenen Bedürfnisse anzupassen, fülle deine Kontext-Dokumente in `context/` aus und passe sie nach Bedarf an. Verwende dann `/create-plan` zum Planen und `/implement` zum Umsetzen struktureller Änderungen. So bleibt alles synchron — besonders CLAUDE.md, die immer den aktuellen Zustand des Workspace widerspiegeln muss.

---

## Session-Workflow

1. **Start**: `/prime` ausführen, um Kontext zu laden
2. **Arbeiten**: Commands verwenden oder Claude direkt mit Aufgaben beauftragen
3. **Änderungen planen**: `/create-plan` vor größeren Ergänzungen verwenden
4. **Umsetzen**: `/implement` zum Ausführen von Plänen verwenden
5. **Pflegen**: Claude aktualisiert CLAUDE.md und context/ während sich der Workspace weiterentwickelt

---

## Notizen

- Kontext minimal aber ausreichend halten — kein Bloat
- Pläne in `plans/` mit datierten Dateinamen für die Historie
- Outputs nach Typ/Zweck in `outputs/` organisiert
- Referenzmaterialien in `reference/` zur Wiederverwendung
