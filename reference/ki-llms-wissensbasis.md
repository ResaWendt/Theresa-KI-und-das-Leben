# KI & LLMs Wissensbasis

> Zusammenfassung der KIPA-Ausbildungsinhalte (Garrit Wilson). Quelle: Obsidian-Notizen "KI LLMs 1a–8b" + Überblicksgrafik (Erklärvideo).

---

## 1. Definition Prompt Engineering

Die **Kunst** und **Wissenschaft**, durch **optimierten Input** mit KI-Modellen **hochqualitative Inhalte** zu erstellen.

- **Kunst:** Hat etwas Intuitives, mit der Zeit bekommt man ein Gefühl dafür, eine Art Momentum wie beim Surfen
- **Wissenschaft:** Unter der Haube Algorithmen und neuronale Netze. Hohe Wahrscheinlichkeit: Input A ergibt Output B

**Mehrwert für Unternehmen:** Hochspezifische Infos eines Unternehmens beziehen, mit der richtigen Technik und Struktur aufbereiten und an ein KI-Modell vermitteln, damit es so arbeiten kann, wie das spezifische Unternehmen es braucht.

**Trends:**
- **Context Engineering:** Die richtigen Informationen bereitstellen, damit das Modell die Aufgabe genau so erledigt, wie das Unternehmen es braucht. Ist der größere Hebel, weil Modelle an sich leistungsfähiger werden.
- **Meta-Prompting:** Ein Modell instruieren, nach eigenen Vorgaben einen Prompt vorzuschreiben (Effizienz-Boost)

**Grundprinzip:** Input → AI Model → Output. Input = Kurzzeitgedächtnis. AI Model = Langzeitgedächtnis (antrainiertes Wissen). Unsere Aufgabe: Das Kurzzeitgedächtnis so modifizieren, dass der gewünschte Output entsteht.

---

## 2. Wie KI-Modelle Fragen beantworten

Das KI-Modell greift auf verschiedene Quellen zu (Prompt Engineering = PE, Context Engineering = CE):

### Vorbestehendes Wissen (PE)
Antrainiertes Wissen in neuronalen Netzen. Achtung: Knowledge Cutoff — inhärentes Wissen geht nur bis zu einem bestimmten Zeitpunkt.

### System Prompt (CE)
Wird vom Modell-Anbieter bei jedem Prompt mitgeschickt. Enthält Instruktionen des Herstellers an das Modell. Beeinflussbar durch:
- **Personalisierung:** Eigene Informationen hinterlegen (nicht im Langzeitgedächtnis, sondern im System Prompt)
- **Erinnerungen:** Modell aggregiert wiederkehrende Inhalte und verankert sie im System Prompt

### Context Window (CE)
Schickt Inhalte aus dem Chatverlauf mit. **Missverständnis:** Wir trainieren ChatGPT nicht! Chatinhalte gehen nicht ins Langzeitgedächtnis, sondern bleiben im Context Window. Heute 200.000–1.000.000 Tokens (ursprünglich nur 4.196 Tokens bei GPT 3.5).

### Chat History (PE)
Modell kann auf gesamte Chat-Historie zugreifen.

### Tools (CE)
Internet-Zugang über Schnittstellen: Online-Recherche, Deep Research, Agentenmodus, Voice Modus, Transkription, Canvas, gpt-image. ChatGPT sendet JSON-Anfragen an APIs.

### RAG — Retrieval Augmented Generation (CE)
Strukturiertes Wissen bereitstellen, auf das das Modell zugreifen kann (z.B. PDFs, Dokumente). Besser als alles in den Prompt zu packen.

### Modellauswahl (PE)
Unterschiedliche Stärken, Schwächen, Verhaltensweisen. Simpelste Unterscheidung: Reasoning-Modelle vs. reguläre LLMs.

### Warum braucht es Prompt Engineering?
- KI-Modelle sind "generell" recht intelligent
- Haben keine SPEZIFISCHE Information
- Teilweise unzuverlässig in Modell- & Tool-Auswahl
- Wir müssen den hochbegabten Praktikanten einweisen

---

## 3. Modell-Entwicklung

- **Finetuning:** Eigener Trainingsdatensatz für die letzten Schichten des Modells. Schärft Ausdrucksweise/Branchenspezifik, stellt aber kein neues Wissen bereit.
- **Reinforcement Learning mit Human Feedback (RLHF):** So lernt ein Baby.
- **Reihenfolge:** Prompting → RAG → Finetuning
- **Neues Wissen:** Braucht RAG (Context Engineering)

---

## 4. Stärken & Schwächen von LLMs

### Stärken
- **Kreativität & Schnelligkeit:** Sehr schnell, sehr viele Ideen
- **Strategische Impulse:** Verschiedene Perspektiven und Meinungen abrufen
- **Skalierbare Personalisierung:** Ein Prompt mit Platzhaltern für verschiedene Kunden
- **Schnelle Texterstellung:** 80%-Lösung, Feinschliff durch Menschen
- **Schnelle Analyse großer Datenbestände:** Unmengen an Infos im Context-Fenster auswerten

### Schwächen
- **Faktische Genauigkeit:** KI ist keine Datenbank. Halluzinationsneigung.
- **Planung und Koordination:** Komplexe Prozesse über längeren Zeitraum noch schwierig
- **Online-Recherche:** Einstieg gut (z.B. Perplexity), aber Quellen selbst checken

---

## 5. Rollen-Metaphern für KI

### Der Praktikant am 1. Tag
Übermenschlich schnell, fleißig, günstig, begabt. ABER: Keine Ahnung von dir, dem Unternehmen, dem spezifischen Prozess, was hohe Qualität bedeutet. Muss ganz genau angewiesen werden.

### Ein LLM ist ein verbaler Taschenrechner
Keine echte Konversation, sondern Mathematik und Wahrscheinlichkeit. Texteingaben werden in Zahlen umgewandelt, berechnet und wieder in Text umgewandelt. **Die Qualität des Ergebnisses hängt zu 100% von den Kompetenzen des Anwenders ab.**

### Achtung Falle: Anthropomorphisieren
KI ist kein Mensch mit eigenem Willen. Hat kein Interesse, das beste Ergebnis zu liefern. Verantwortung für das Ergebnis nie abgeben!

---

## 6. KI trainieren — was wirklich passiert

LLMs trainieren braucht Doktoranden, riesige Datensätze, 100+ Mio. USD. Wir trainieren ChatGPT NICHT (Ausnahme: Finetuning).

Informationen werden unterschiedlich gespeichert:
- Kurzzeitgedächtnis: System Prompt, Context Window, Personalisierung, Erinnerung
- Gezielt bereitgestellt: RAGs etc.

Personalisierung in deinem Account ≠ Training des Modells. Deine Daten werden nicht im Account anderer ausgespielt.

---

## 7. Limitationen

### Halluzinationen
Tendenz, mit viel Selbstbewusstsein falsche oder irreführende Ergebnisse zu generieren. Gegenmaßnahmen:
- **Human-in-the-Loop:** Mensch prüft Endergebnis (soziotechnische Systeme)
- **Grounding:** Wissensdatenbank bereitstellen (RAG). Reduziert, aber verhindert Halluzination nicht zu 100%.

### Variabilität
Nicht 100% vorhersagbar, probabilistisch. Gegenmaßnahme:
- **Resampling:** Mehrfach generieren, bestes Ergebnis wählen
- **Hyperparameter:** Temperatur, top_p anpassen

### Knowledge Cutoff
Wissen nur bis Trainingsende. Heute durch Internet-Zugang weitgehend kompensiert.

### Context Window
Heute 200–400K Tokens, kein echtes Problem mehr.

### Datenschutz
Externe Limitation, mit **Privacy by Design** begegnen.

---

## 8. Das Problem beim Prompten

### Deterministisch vs. Probabilistisch
- **Software:** Deterministisch (A → B, immer)
- **KI-Modelle:** Probabilistisch (A → B / C / D, basiert auf Wahrscheinlichkeit)

### Kreative vs. produktive Anwendungsfälle
- **Kreativ:** Idee vorhanden, Endergebnis unklar. Variabilität ist hilfreich.
- **Produktiv:** Endergebnis klar, hohe Qualität gefragt. Vorhersagbare Ergebnisse nötig.

### Das Kernproblem
Modelle liefern die wahrscheinlichste Antwort = Durchschnitt = generisch. **Unsere Aufgabe: Das natürliche Verhalten so steuern, dass überdurchschnittlich gute Ergebnisse entstehen.**

---

## 9. Prompting-Herangehensweisen

### 1) Unterhaltung
Keine Aufgabe, kein spezifisches Ergebnis → Dialog

### 2) Kreativ
Genaue Aufgabe, Ergebnis unbekannt → **Conversational Prompting** (explorativer Prozess mit dem KI-Modell, gemeinsam Lösungen finden)

### 3) Produktiv
Genaue Aufgabe, genaue Anforderungen → **Single Shot Prompting** (ein Prompt liefert auf Knopfdruck fertiges Ergebnis)

---

## 10. Die drei Prompting-Prinzipien (Lösung für schlechte Qualität)

### Struktur
Prompts korrekt strukturieren, damit das KI-Modell Instruktionen optimal auslesen kann.

### Spezifizität
Sehr hoher Grad an Spezifizität. Modell weiß nicht, wer du bist, wer dein Kunde ist, worauf es ankommt. Diese Infos müssen wir bereitstellen und Schritt für Schritt anleiten.

### Kontext
Kontextuelle Informationen bereitstellen, damit das Modell zum richtigen Zeitpunkt auf die richtige Information zugreifen kann.

**RECAP:** Hochspezifische Single-Shot-Prompts erstellen, maximal optimiert mit richtiger Struktur, hohem Grad an Spezifizität und den richtigen Informationen, damit das KI-Modell auf Knopfdruck hochqualitative Ergebnisse liefert.

---

## 11. Prompt Development Zyklus

### 1. Analyse
Bei produktiven Anwendungsfällen: Grundlegende, umfassende Analysephase. Verstehen, was hochqualitative Ergebnisse ausmacht. Anforderungsprofil mit dem Kunden erstellen (90 Min – 2 Std).

### 2. Anforderungsprofil
Muster/Beispiel/Vorlage des Kunden. Überarbeitung gemäß Prinzipien (Struktur, Spezifizität, Kontext).

### 3. Prompt Draft
Wissen über Anforderungsprofil über Prompting-Techniken verankern. Iterativer Prozess mit Feedbackschleifen.

### 4. Testphase
3–4 Iterationen (kann Wochen dauern). Output gegen Anforderungsprofil prüfen, Prompt optimieren. Promptchains für komplexe Aufgaben. Kunde testet selbst und gibt Feedback.

---

## 12. Prompt-Formatierung

Professionelle Prompts im **Markdown**-Format. Gliederung in Abschnitte mit Überschriften. Auch System Prompts der Hersteller sind in Markdown formatiert.

---

## 13. Prompting-Techniken

> Jede Technik erhöht die Wahrscheinlichkeit eines guten Ergebnisses. Ergebnisqualität hängt aber vor allem von den Prinzipien ab (Struktur, Spezifizität, Kontext).

**WICHTIG: Nie im gleichen Chatfenster durchprompten, immer neues Fenster öffnen!**

### Basic Prompt
`Schreibe einen LinkedIn Post zu folgendem Thema: [Thema]`

### Role Prompting
Dem Modell eine Rollenidentifikation vorgeben mit der benötigten Kompetenz.
`Rolle: Du bist [Rolle + Beschreibung]`

### Kontext
Setting the Scene — Bühnenbild kreieren, Praktikant ins Unternehmen einführen.
`Kontext: Aktuell bist du dabei, [Prozess]. Unser Ziel ist es, [Ziel]. Das ist wichtig, weil [Beschreibung].`

### Aufgabenbeschreibung + Chain of Thought
Ganz konkret, wie die Aufgabe zu erledigen ist. Schritt-für-Schritt-Anleitung.
`Aufgabe: Deine Aufgabe ist es jetzt, [Beschreibung]. Gehe dabei wie folgt vor: 1. … 2. … 3. …`

### Input Information
Dem Modell sagen, um welche Art von Info es sich handelt.
`Inhalt: Schreibe den Beitrag nur über folgenden Inhalt: <inhalt>[Inhalt]</inhalt>`

### Beispiele
Hochqualitative Beispiele bereitstellen.
`Beispiel: Du bekommst hier Beispiele für hochqualitative [Ergebnisse]. Verwende denselben Stil und dasselbe Format, ohne Inhalte zu übernehmen. <beispiele>[Beispiele]</beispiele>`

### Style Guidance
`Stil: Dein Stil ist geprägt durch [Beschreibung des Stils].`

### Format
`Format: Achte darauf, immer die folgende Formatierung zu verwenden: [Elemente]`

### Anweisungen
`Anweisungen: Achte darauf, immer [...]. Niemals darfst du [...].`

---

## 14. Self Evaluation Prompting

KI-Modell bewertet den Output eines anderen KI-Modells (oder den eigenen). Anwendung:
- Checkliste erstellen → Output gegen Checkliste bewerten → Verbesserungsvorschläge → Überarbeitete Version
- Bei Automatisierungen: Zusätzliches KI-Modul in der Kette zur Qualitätsprüfung
- Bei Klassifizierungsaufgaben: Prüfung ob Kategorisierung korrekt

---

## 15. Lost-in-the-Middle Effect

Modelle verarbeiten **Anfang** und **Ende** eines Prompts zuverlässiger als den **Mittelteil**.

### Best Practices
1. Wichtigstes an den **Anfang** (Ziel, Rolle, Ergebnisformat)
2. Wichtigstes am **Ende wiederholen** (doppelte Verankerung)
3. Mittelteil entlasten (Stichpunkte statt lange Erklärungen)
4. Struktur > Textmenge (nummerierte Regeln statt Fließtext)
5. Kritische Regeln markieren (WICHTIG, NICHT, IMMER, AUF KEINEN FALL)
6. Modular prompten: Rolle + Ziel → Regeln → Aufgabe → iterativ nachschärfen

---

## 16. Grounding & Parameter

### Temperatur
Bestimmt, wie zufällig/fokussiert Antworten sind (0–1).
- **Niedrig:** Wahrscheinlichstes Wort, präzise, strukturiert
- **Hoch:** Auch weniger wahrscheinliche Wörter, kreativ, abwechslungsreich

### top_p
Bestimmt, wie breit aus der Wahrscheinlichkeitsverteilung ausgewählt wird.
- Niedriger top_p: Engere Auswahl
- top_p = 1: Gesamte Verteilung

**ChatGPT-Einstellungen:** 0,3 temperature (sachlich), 0,8 top_p (größere Bandbreite)

### Anwendung
- **Kreative Aufgaben:** Höhere Temperatur (Brainstorming, neue Ideen)
- **Produktive Aufgaben:** Niedrigere Temperatur (Dokumentation, Anforderungen)

---

## 17. GPTs (Custom ChatGPT Versionen)

Eigene ChatGPT-Versionen mit vorgegebenen Instruktionen. Verhält sich immer gleich.

- **ChatGPT:** Muss immer wieder neu angewiesen werden
- **GPT:** Wie ein eingearbeiteter Mitarbeiter

### Bestandteile
1. **Instructions:** Arbeitsanweisung (Prompt im Markdown-Format)
2. **Knowledge Base:** Unterlagen zur Aufgabenerfüllung

Für Prozesse mit mehreren Teilaufgaben: Mehrere GPTs erstellen, die in einem Chat zusammenarbeiten.

---

## 18. Prompting für Klassifizierungsaufgaben

Prompt klassisch aufgebaut (Rolle, Kontext, Aufgabe, Beispiele). **Wichtigste Sektion: Beispiele.**

- **Few-Shot Learning:** Anhand von Beispielen im Prompt lernt das Modell die Zuordnung
- Pro Kategorie mindestens 3 Beispiele, durchmischt
- Echte, anonymisierte Beispiele verwenden
- Mit Reasoning-Modell arbeiten
- Mit anderem KI-Modell Klassifizierung überprüfen
- Testen, testen, testen!

---

## 19. KI-Tools im Überblick

### ChatGPT (OpenAI)
Über 1 Mrd. Nutzer/Monat (2025). Modalitäten: Einfacher Prompt, Online-Recherche, Graphen, Bilder, Audiomodus, Canvas, Projekte.

### Claude (Anthropic)
Bestes Modell für Codeerstellung und Copywriting. Features: Artifacts (mächtiger als Canvas bei Code), Explain Feature, Projects (vergleichbar mit GPT-Feature).

### Google AI Studio
Hochperformant. Experimental: bis 1 Mio. Tokens, ganze Bücher und Videos. Flash Thinking (Reasoning). Screen-Sharing für Live-Feedback.

### Gemini App
Nicht empfehlenswert.

---

## 20. Case Study: LinkedIn-Post mit Conversational Prompting

Schrittweiser Aufbau einer Prompt-Chain:

1. **Rolle definieren:** Welche Rolle eignet sich für Social-Media-Beiträge?
2. **Art des Beitrags:** Post-Typ festlegen (z.B. Personal Story Post), Ziele erarbeiten
3. **Copywriting Frameworks recherchieren** (z.B. AIDA)
4. **Post-Struktur** nach gewähltem Framework erstellen
5. **Checkliste** aus allen Elementen erstellen
6. **Post erstellen** mit komplettem Prompt (Aufgabe, Inhalt, Beispiele, Schreibstil, Anweisungen)
7. **Evaluierung** anhand der Checkliste, Verbesserungsvorschläge, überarbeitete Version

Empfehlung: 3 Durchläufe über "Erneut versuchen"-Button, dann Evaluierung.

---

*Zusammengestellt aus: Obsidian-Notizen KI LLMs 1a–8b + Überblicksgrafik (Erklärvideo)*
*Quellen: KIPA (Garrit Wilson), Anforderungsfabrik, K2view, GitHub Leaderboards*
*Stand: 2026-03-18*
