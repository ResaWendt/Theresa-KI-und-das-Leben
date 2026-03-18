# Schulung Prompting für Michaela

> Mini-Einschulung Prompting | 90 Minuten | Termin: 20.03.2026
> Teilnehmerin: Michaela (arbeitet in der Werbung/Werbeagentur)
> Trainerin: Theresa Wendt

---

## Ziel der Schulung

Michaela soll nach der Schulung:
- Verstehen, wie KI-Modelle funktionieren und wo ihre Grenzen liegen
- Eigenständig gute Prompts für ihren Werbe-Alltag schreiben können
- Die drei Prompting-Prinzipien (Struktur, Spezifizität, Kontext) anwenden
- Wissen, wann Conversational vs. Single Shot Prompting sinnvoll ist
- ChatGPT und Claude für Werbetexte, Konzepte und Kampagnen nutzen können

---

## Überblick: 5 Blöcke

| Block | Thema | Dauer | Methode |
|---|---|---|---|
| 1 | Wie KI-Modelle funktionieren | 15 Min | Erklärung + Überblicksgrafik |
| 2 | Stärken, Schwächen & die richtige Erwartung | 10 Min | Erklärung + Diskussion |
| 3 | Die drei Prompting-Prinzipien | 20 Min | Erklärung + Live-Demo |
| 4 | Prompting-Techniken für die Praxis | 25 Min | Gemeinsam prompten |
| 5 | Michaelas Anwendungsfall: Werbung | 20 Min | Hands-on Übung |

**Gesamt: 90 Minuten**

---

---

# BLOCK 1: Wie KI-Modelle funktionieren (15 Min)

---

## Lernziel

Michaela versteht, was "unter der Haube" passiert und warum ihre Eingabe so wichtig ist.

## Einstieg (2 Min)

**Theresa sagt sinngemäß:**

> Bevor wir anfangen, Prompts zu schreiben, will ich dir kurz zeigen, wie das Ganze eigentlich funktioniert. Nicht technisch im Detail, aber so, dass du verstehst, warum manche Prompts gute Ergebnisse liefern und manche nicht. Wenn du weißt, wie das Modell "denkt", kannst du es viel gezielter einsetzen.

## Das Grundprinzip (3 Min)

**Grafik zeigen: Bild 1** — Was der Nutzer sieht.

> Das hier ist, was du siehst, wenn du ChatGPT öffnest. Du tippst eine Frage ein, die KI antwortet. Simpel. Aber dahinter passiert einiges mehr.

**Das Prinzip an der Tafel/Bildschirm aufschreiben:**

```
Input  -->  KI-Modell  -->  Output
```

> Das KI-Modell hat zwei Gedächtnisse:
> - **Langzeitgedächtnis** = Das antrainierte Wissen. Da stecken Milliarden von Texten drin, aus denen das Modell gelernt hat. Das ist fix und du kannst es nicht verändern.
> - **Kurzzeitgedächtnis** = Alles, was du ihm in diesem Moment mitgibst. Dein Prompt, dein Kontext, deine Beispiele.
>
> Unsere Aufgabe ist es, das Kurzzeitgedächtnis so gut zu füllen, dass der Output genau das ist, was wir brauchen.

## Die Überblicksgrafik Schritt für Schritt (8 Min)

Jetzt die Bilder der Überblicksgrafik nacheinander durchgehen. Jedes Bild erklärt eine Schicht, die das Modell beeinflusst.

### Schicht 1: Vorbestehendes Wissen

**Grafik zeigen: Bild 2 + 3** — Der große Kreis = antrainiertes Wissen.

> Siehst du den großen Kreis? Das ist das antrainierte Wissen. Das ist quasi das Gehirn des Modells. Da steckt alles drin, was es je gelernt hat, Bücher, Webseiten, Artikel, Code. Aber: Es gibt einen Knowledge Cutoff. Das heißt, das Wissen geht nur bis zu einem bestimmten Datum. Was danach passiert ist, weiß das Modell nicht, es sei denn, es greift aufs Internet zu.

### Schicht 2: System Prompt

**Grafik zeigen: Bild 4** — System Prompt erscheint.

> Jetzt wird es spannend. Bevor du überhaupt etwas eingibst, schickt der Hersteller, also OpenAI bei ChatGPT, bei jeder einzelnen Anfrage einen System Prompt mit. Das ist ein Prompt mit ganz vielen Instruktionen, wie sich das Modell verhalten soll. Du siehst den nie. Aber er ist immer da.
>
> Zum Beispiel steht da drin: "Du bist ChatGPT, ein großes Sprachmodell von OpenAI. Sei hilfreich." Und noch viel mehr.

### Schicht 3: Personalisierung

**Grafik zeigen: Bild 5** — Personalisierung + Erinnerungen.

> Jetzt kannst du den System Prompt aber beeinflussen. Und zwar über die Personalisierung in den Einstellungen. Da kannst du hinterlegen, wer du bist, in welcher Branche du arbeitest, welchen Schreibstil du bevorzugst.
>
> Und dann gibt es noch die Erinnerungen. Wenn du mit ChatGPT immer wieder über die gleichen Themen sprichst, merkt es sich das und verankert es im System Prompt. Das kannst du in den Einstellungen anschauen und auch löschen.

**Tipp für Michaela:**
> Geh mal in die Einstellungen von ChatGPT und schau, was da unter Personalisierung und Erinnerungen steht. Und dann hinterlege dort ein paar Sätze über dich und deine Arbeit: "Ich bin Werbetexterin in einer Agentur in Österreich. Ich schreibe Texte für Print, Online und Social Media. Meine Kunden sind [Branchen]. Meine Sprache ist Deutsch."

### Schicht 4: Context Window

**Grafik zeigen: Bild 6** — Context Window mit Chat-Verlauf.

> Das Context Window ist das Kurzzeitgedächtnis. Alles, was in deinem aktuellen Chat steht, fließt da rein. Deine Fragen, die Antworten der KI, alles. Heute sind die Context Windows riesig, 400.000 Tokens bei ChatGPT, das sind ungefähr 300.000 Wörter, ein ganzes Buch.
>
> **Aber Achtung, das ist ein ganz wichtiges Missverständnis:** Wir trainieren ChatGPT NICHT. Die Inhalte deines Chats gehen nicht in das Langzeitgedächtnis. Die bleiben nur in diesem einen Chat-Fenster. Wenn du ein neues Chat-Fenster öffnest, fängst du bei null an.

### Schicht 5: Chat History

**Grafik zeigen: Bild 8** — Chat History separat.

> Das Modell kann aber auch auf deine vergangenen Chats zugreifen, die Chat History. Das ist getrennt vom Context Window. Stell dir vor, du hast letzte Woche einen Chat über Kampagne X geführt. ChatGPT kann sich daran erinnern, wenn du danach fragst.

### Schicht 6: Tools

**Grafik zeigen: Bild 9** — Tools-Übersicht.

> ChatGPT kann mehr als nur Text. Es hat Tools:
> - **Online-Recherche / Deep Research:** Greift aufs Internet zu, holt aktuelle Infos
> - **Voice Modus / Transkription:** Sprachein- und -ausgabe
> - **Canvas:** Zum Bearbeiten von Texten, sehr praktisch für längere Werbetexte
> - **Bildgenerierung (gpt-image):** Bilder erstellen
>
> Für dich als Werbetexterin besonders interessant: Canvas zum Feinschliff von Texten und die Bildgenerierung für Konzept-Visualisierungen.

### Schicht 7: RAG

**Grafik zeigen: Bild 10** — RAG hinzugefügt.

> RAG steht für Retrieval Augmented Generation. Klingt kompliziert, ist aber simpel: Du stellst dem Modell eigene Dokumente zur Verfügung, auf die es zugreifen kann. Zum Beispiel ein Kunden-Briefing als PDF, eine Markenstrategie oder Textbeispiele.
>
> Das ist viel stabiler, als alles in den Prompt zu packen. Bei ChatGPT geht das über Projekte oder GPTs, da lädst du Dateien hoch.

### Schicht 8: Modellauswahl

**Grafik zeigen: Bild 11** — Mehrere Modelle.

> Und dann gibt es noch verschiedene Modelle. Nicht jedes Modell ist gleich gut für jede Aufgabe.
> - **ChatGPT (OpenAI):** Der Allrounder, über 1 Milliarde Nutzer
> - **Claude (Anthropic):** Bestes Modell für Copywriting und Code
> - **Google AI Studio:** Experimentell, riesiges Context Window
>
> Für Werbetexte ist Claude oft die bessere Wahl. Für Recherche ChatGPT. Am besten: Beide ausprobieren.

### Prompt Engineering vs. Context Engineering

**Grafik zeigen: Bild 13 + 14 + 15** — Rote und orange Punkte.

> Jetzt siehst du in der Grafik rote und orange Punkte.
> - **Rot = Prompt Engineering:** WIE wir fragen, also die Formulierung unserer Eingabe
> - **Orange = Context Engineering:** WELCHE Informationen wir bereitstellen, also System Prompt, Personalisierung, RAG, Dokumente
>
> Der Trend geht klar Richtung Context Engineering. Die Modelle werden von selbst immer schlauer. Der größere Hebel ist mittlerweile, ihnen die richtigen Informationen zu geben.

### Warum braucht es Prompt Engineering?

**Grafik zeigen: Bild 12** — Die vier Gründe.

> Trotzdem braucht es Prompt Engineering, weil:
> 1. KI-Modelle sind "generell" recht intelligent, ABER...
> 2. sie haben keine SPEZIFISCHE Information über dich und dein Projekt
> 3. sie sind teilweise unzuverlässig in der Modell- und Tool-Auswahl
> 4. Wir müssen den hochbegabten Praktikanten einweisen

## Die zwei Metaphern (2 Min)

### Metapher 1: KI = Hochbegabter Praktikant am 1. Tag

> Stell dir vor, du bekommst einen neuen Praktikanten. Der ist übermenschlich schnell, unfassbar fleißig, spricht alle Sprachen und kostet fast nichts. Aber: Er hat keine Ahnung von deiner Agentur, kennt deine Kunden nicht, weiß nicht was "guter Werbetext" für euch bedeutet. All das musst du ihm erst beibringen. Und zwar ganz genau, wie jemanden, der etwas zum allerersten Mal macht.
>
> Wenn du ihm sagst "Schreib mal was Cooles für den Kunden", bekommst du irgendwas. Wenn du ihm sagst "Schreib einen Facebook-Post für [Kunde], Zielgruppe [X], Tonalität [Y], mit diesem Call-to-Action, in diesem Format", bekommst du was Brauchbares.

### Metapher 2: LLM = Verbaler Taschenrechner

> Es fühlt sich an wie eine Konversation, aber unter der Haube ist es nur Mathematik. Deine Texteingabe wird in Zahlen umgewandelt, ein Algorithmus berechnet die wahrscheinlichste Fortsetzung, und die Zahlen werden wieder in Text umgewandelt.
>
> Und genau wie beim Taschenrechner gilt: Wie gut das Ergebnis ist, hängt zu 100% vom Anwender ab. Nicht vom Rechner.

### Achtung Falle: Anthropomorphisieren

> Es ist total verführerisch, zu denken, dass ChatGPT dich versteht, dass es dir helfen WILL. Tut es nicht. Es hat keinen eigenen Willen und kein Interesse daran, dir das beste Ergebnis zu liefern. Es liefert das wahrscheinlichste Ergebnis. Das ist ein Unterschied. Die Verantwortung für das Ergebnis liegt immer bei dir.

## Kernbotschaften Block 1

- KI ist kein Mensch, kein Google, keine Datenbank
- Verantwortung für das Ergebnis nie abgeben
- Je besser dein Input, desto besser der Output
- Wir trainieren ChatGPT nicht, wir füttern das Kurzzeitgedächtnis

**Überleitung:** *"Jetzt wo du weißt wie das funktioniert, schauen wir uns an, was KI gut kann und wo du aufpassen musst."*

---

---

# BLOCK 2: Stärken, Schwächen & die richtige Erwartung (10 Min)

---

## Lernziel

Michaela weiß, wofür sie KI im Werbe-Alltag einsetzen kann und wo Vorsicht geboten ist.

## Stärken von KI -- was für dich relevant ist (4 Min)

**Theresa sagt sinngemäß:**

> Jetzt die guten Nachrichten. Wo ist KI richtig stark und wo hilft sie dir im Alltag?

### 1. Kreativität & Schnelligkeit

> KI kann in Sekunden 20 Headline-Varianten ausspucken. Wenn du für einen Kunden einen Slogan brauchst, kannst du in 5 Minuten mehr Ideen generieren als in einem einstündigen Brainstorming. Nicht jede Idee ist Gold, aber darunter sind fast immer 2-3 Ansätze, auf denen du aufbauen kannst.

**Konkretes Beispiel:**
> Stell dir vor, du brauchst Headlines für eine Print-Kampagne für ein Wiener Restaurant. Du gibst dem Modell: das Restaurant, die Zielgruppe, den Anlass, die Tonalität, und sagst "Gib mir 15 Headline-Varianten." In unter einer Minute hast du 15 Vorschläge. Davon nimmst du die besten 3 und arbeitest die weiter aus.

### 2. Skalierbare Personalisierung

> Du schreibst einen richtig guten Prompt für einen Newsletter-Text. Dann tauschst du nur den Kunden aus, alles andere bleibt gleich. Du hast quasi eine Textmaschine, die für verschiedene Kunden personalisierte Texte ausspuckt, alle im gleichen Qualitätsstandard.

### 3. Schnelle Texterstellung (80%-Lösung)

> KI liefert in den meisten Fällen eine solide 80%-Lösung. Die letzten 20% sind dein Job: Feinschliff, Markenstimme reinbringen, das gewisse Etwas. Aber die 80% in 2 Minuten statt in 2 Stunden zu haben, das ist der Hebel.

### 4. Strategische Impulse

> Du kannst ChatGPT nach verschiedenen Perspektiven fragen. "Wie würde ein Marketingleiter in der Tourismusbranche darauf reagieren?" oder "Welche Einwände hätte die Zielgruppe 50+?" Das Modell kann verschiedene Blickwinkel simulieren, die du für Kampagnenkonzepte nutzen kannst.

### 5. Analyse

> Du bekommst ein 20-seitiges Briefing vom Kunden? Lade es hoch und sag: "Fasse die Key Messages zusammen und identifiziere die drei stärksten Selling Points." Das spart dir eine Stunde Lesen und Sortieren.

## Schwächen -- wo du aufpassen musst (3 Min)

> Jetzt die weniger guten Nachrichten. Es gibt drei Dinge, bei denen KI dich in die Irre führen kann.

### 1. Faktische Genauigkeit -- KI halluziniert

> KI ist KEINE Datenbank. Wenn du fragst "Wie viele Einwohner hat Graz?", bekommst du wahrscheinlich eine richtige Antwort. Aber wenn du fragst "Wie hoch war der Umsatz von Firma X im letzten Jahr?", kann es sein, dass ChatGPT dir mit absolutem Selbstbewusstsein eine Zahl nennt, die komplett erfunden ist. Das nennt man Halluzination.
>
> **Für dich konkret:** Zahlen, Fakten, Statistiken, Zitate in Werbetexten IMMER gegenchecken. Nie blind übernehmen.

### 2. Generische Ergebnisse -- das Kernproblem

> Das ist der wichtigste Punkt. KI-Modelle sind darauf optimiert, die wahrscheinlichste Antwort zu liefern. Die wahrscheinlichste Antwort ist per Definition der Durchschnitt. Und Durchschnitt in der Werbung ist tödlich. Generisch, austauschbar, geht unter.
>
> Wenn du ChatGPT einfach sagst "Schreib mir einen Werbetext", bekommst du einen Text, der so klingt, wie alle Werbetexte zusammen klingen. Glatt. Langweilig. Ohne Ecken und Kanten.
>
> **Unsere Aufgabe heute: Lernen, wie wir durch gute Prompts aus diesem Durchschnitt herauskommen und überdurchschnittliche Ergebnisse bekommen.**

### 3. Online-Recherche -- mit Vorsicht genießen

> ChatGPT kann im Internet recherchieren, aber die Ergebnisse sind nicht immer objektiv. OpenAI hat Verträge mit bestimmten Medienhäusern, deren Inhalte werden bevorzugt ausgespielt. Für einen ersten Überblick okay, aber Quellen immer selbst prüfen.

## Umgang mit Limitationen (3 Min)

> Wie gehen wir mit diesen Schwächen um? Drei Strategien:

### 1. Human-in-the-Loop

> Du bist immer der letzte Check. KI erstellt den Entwurf, DU prüfst und finalisierst. Das ist nicht optional, das ist Pflicht. Wir bauen hier soziotechnische Systeme, Mensch und Maschine arbeiten zusammen. Das sind die stabilsten Lösungen.

### 2. Resampling

> Wenn du einen guten Prompt hast, generiere 3x und nimm das beste Ergebnis. Weil KI probabilistisch arbeitet, also auf Wahrscheinlichkeiten basiert, kommt nicht jedes Mal das gleiche raus. Manchmal ist der zweite oder dritte Durchlauf besser.

### 3. Nie blind vertrauen

> Besonders bei: Zahlen, Fakten, Zitaten, rechtlichen Aussagen. Immer gegenchecken.

**Überleitung:** *"Gut, du weißt jetzt was KI kann und wo die Grenzen sind. Jetzt zeig ich dir, wie du Prompts schreibst, die wirklich gute Ergebnisse liefern."*

---

---

# BLOCK 3: Die drei Prompting-Prinzipien (20 Min)

---

## Lernziel

Michaela kennt die drei Prinzipien und kann sie auf ihre Prompts anwenden. Sie sieht den Unterschied zwischen einem schlechten und einem guten Prompt live am Bildschirm.

## Die zwei Probleme (3 Min)

**Theresa sagt sinngemäß:**

> Es gibt zwei Probleme, die fast alle haben, wenn sie mit KI arbeiten.

### Problem I: Schlechte Qualität

> Du promptest, und das Ergebnis ist... naja. Generisch. Klingt wie von einer KI geschrieben. Nicht das, was du brauchst. Warum? Weil das Modell ohne gute Anweisung einfach den Durchschnitt liefert. Es gibt das wahrscheinlichste Ergebnis, und das ist per Definition mittelmäßig.

### Problem II: Fehlende Systematisierung

> Du hast vielleicht mal durch Hin- und Herschreiben mit ChatGPT einen brauchbaren Text bekommen. Aber wie willst du das wiederholen? Wie willst du das an eine Kollegin weitergeben? Es skaliert nicht. Es ist nicht reproduzierbar. Und du verbringst jedes Mal 30 Minuten mit Chatten, statt in 2 Minuten ein Ergebnis zu haben.

> Für beide Probleme gibt es eine Lösung. Drei Prinzipien.

## Die drei Prinzipien (7 Min)

### Prinzip 1: Struktur

> Professionelle Prompts sind keine Chatnachrichten. Sie sind strukturiert wie Dokumente. Mit Überschriften, Abschnitten und klaren Trennungen.

> Warum? Weil KI-Modelle Markdown-Formatierung verstehen und darauf optimiert sind. Der System Prompt, den der Hersteller mitschickt, ist auch im Markdown-Format. Wenn du deinen Prompt genauso strukturierst, kann das Modell deine Instruktionen optimal auslesen.

**Am Bildschirm zeigen, wie ein strukturierter Prompt aussieht:**

```
Unstrukturiert (schlecht):
"Schreib einen Text für meinen Kunden der ein Restaurant hat
und der soll lustig sein und auf Facebook gepostet werden
und ungefähr 150 Wörter"

Strukturiert (gut):
# Rolle
Du bist ein erfahrener Social-Media-Texter.

# Aufgabe
Schreibe einen Facebook-Post für ein Wiener Restaurant.

# Format
- Länge: max. 150 Wörter
- Tonalität: humorvoll, wienerisch

# Anweisungen
- Verwende einen starken Einstiegssatz
- Schließe mit einem Call-to-Action
```

> Siehst du den Unterschied? Gleiche Information, aber das Modell kann die strukturierte Version viel besser verarbeiten.

### Prinzip 2: Spezifizität

> Das Modell hat zwar generell einen hohen Grad an Intelligenz, aber es hat keine Ahnung, wer du bist, wer dein Kunde ist und worauf es bei DIESER Aufgabe, für DIESES Unternehmen, in DIESEM Moment ankommt.

> Je spezifischer du bist, desto besser das Ergebnis. Statt "Schreib einen Werbetext" sagst du GENAU:
> - WAS: Ein Facebook-Post
> - FÜR WEN: Restaurant Zum Goldenen Schnitzel, Wiener Traditionsküche, seit 1985
> - ZIELGRUPPE: Wiener 35-55, genussaffin, schätzen Tradition
> - TONALITÄT: Warmherzig, mit einem Augenzwinkern, wienerisch
> - ZIEL: Tischreservierungen für Ostersonntag
> - FORMAT: Max. 150 Wörter, mit Emoji aber nicht übertrieben

> Merkst du wie viel mehr Information das ist? Und genau diese Spezifizität ist der Unterschied zwischen "geht so" und "wow".

**Michaela fragen:**
> Denk mal kurz an einen Kunden von dir. Welche Informationen bräuchte ein Praktikant, der diesen Kunden zum ersten Mal betreut, um einen guten Text zu schreiben?

*(Kurzer Austausch, 2 Min. Michaela nennt Infos, die sie normalerweise braucht. Theresa zeigt: Genau DAS musst du auch dem Modell mitgeben.)*

### Prinzip 3: Kontext

> Kontext ist alles, was das Modell braucht, um deine spezifische Situation zu verstehen. Das geht über Spezifizität hinaus: Es sind die Hintergrundinformationen, die Beispiele, die Referenzen.

> Konkret:
> - Wer ist der Kunde? (Branche, Größe, Philosophie)
> - Wer ist die Zielgruppe? (Demografie, Psychografie, Pain Points)
> - Wie soll es klingen? (Beispiele! Bisherige Texte!)
> - Was ist der Rahmen? (Kanal, Budget, Zeitraum)

> Besonders wichtig: **Beispiele mitgeben**. Wenn du dem Modell drei gute Facebook-Posts zeigst, die der Kunde bereits hatte, versteht es den Stil 10x besser als jede Beschreibung.

**Zusammenfassung auf einen Blick:**

| Prinzip | Frage | Beispiel |
|---|---|---|
| **Struktur** | Ist mein Prompt klar gegliedert? | Überschriften, Abschnitte, Listen |
| **Spezifizität** | Weiß das Modell genau, was ich will? | WAS, FÜR WEN, WIE, WOZU |
| **Kontext** | Hat das Modell alle Infos, die es braucht? | Beispiele, Briefing, Zielgruppe |

## Live-Demo: Schlecht vs. Gut (10 Min)

> Jetzt zeig ich dir den Unterschied live. Wir geben ChatGPT zwei Prompts und vergleichen die Ergebnisse.

### Demo-Prompt 1: Ohne Prinzipien (schlecht)

**In ChatGPT eingeben:**

```
Schreib mir einen Werbetext für ein Restaurant.
```

> *(Ergebnis zeigen, gemeinsam besprechen)* Siehst du? Generisch. Könnte jedes Restaurant auf der Welt sein. Kein Charakter, keine Persönlichkeit, austauschbar. Genau das meine ich mit "Durchschnitt".

### Demo-Prompt 2: Mit allen drei Prinzipien (gut)

**In ChatGPT eingeben:**

```markdown
# Rolle
Du bist ein erfahrener Werbetexter, spezialisiert auf Gastronomie
in Wien. Du kennst den Wiener Schmäh und weißt, wie man Genuss-
menschen anspricht.

# Kontext
Dein Kunde ist "Zum Goldenen Schnitzel", ein Wiener Traditionshaus
seit 1985. Familienbetrieb, 3. Generation. Bekannt für das beste
Wiener Schnitzel der Stadt (Kalbfleisch, handgeklopft, in Butter
ausgebacken). Zielgruppe: Wiener und Wien-Besucher, 35-60,
genussaffin, schätzen Qualität und Tradition.

# Aufgabe
Schreibe einen Facebook-Post für den Osterbrunch am 20. April.
Gehe dabei wie folgt vor:
1. Starte mit einem aufmerksamkeitsstarken ersten Satz
2. Beschreibe das Oster-Special (Brunch-Buffet mit Schnitzel-
   Station, hausgemachte Mehlspeisen, Aperol Spritz zur Begrüßung)
3. Nenne Preis (€ 39 pro Person) und Reservierungshinweis
4. Schließe mit einem einladenden Call-to-Action

# Stil
Warmherzig, mit einem Augenzwinkern. Wiener Schmäh, aber nicht
aufgesetzt. So als würde der Wirt persönlich einladen. Keine
Werbefloskeln wie "einzigartig" oder "unvergesslich".

# Format
- Max. 150 Wörter
- Kurze Absätze (max. 2-3 Zeilen)
- 1-2 passende Emojis, nicht übertrieben
- Reservierungslink am Ende: www.goldenes-schnitzel.at/ostern

# Anweisungen
- Schreibe auf Deutsch (österreichisches Deutsch)
- Vermeide generische Gastro-Floskeln
- Das Schnitzel ist der Star, nicht der Brunch allgemein
- KEIN "Lass dir das nicht entgehen" oder ähnliche Phrasen
```

> *(Ergebnis zeigen, gemeinsam besprechen)* Merkst du den Unterschied? Das klingt nach diesem Restaurant. Das hat Charakter. Das könnte man so posten.
>
> Und jetzt stell dir vor: Du änderst nur den Kunden, das Restaurant und das Angebot, aber die Struktur bleibt gleich. Das ist der Hebel.

**Überleitung:** *"Cool, oder? Jetzt zeig ich dir die einzelnen Bausteine, aus denen so ein Prompt zusammengesetzt ist, damit du das selbst bauen kannst."*

---

---

# BLOCK 4: Prompting-Techniken für die Praxis (25 Min)

---

## Lernziel

Michaela kennt die Prompt-Bausteine und die zwei Herangehensweisen (Conversational vs. Single Shot). Sie baut ihren ersten eigenen Prompt mit allen Bausteinen.

## Zwei Herangehensweisen (5 Min)

**Theresa sagt sinngemäß:**

> Es gibt zwei grundsätzlich verschiedene Wege, wie du mit KI arbeiten kannst. Und welchen du wählst, hängt davon ab, ob du schon weißt, wie das Ergebnis aussehen soll oder nicht.

### Conversational Prompting (für kreative Anwendungsfälle)

> Wenn du noch NICHT genau weißt, wie das Endergebnis aussehen soll. Zum Beispiel: "Wir brauchen eine Kampagnenidee für Kunde X, aber wir wissen noch nicht, in welche Richtung es gehen soll."
>
> Dann arbeitest du Schritt für Schritt MIT dem Modell. Du gibst die Richtung vor, das Modell liefert Impulse, du steuerst weiter. Ein gemeinsamer Denkprozess.

**Beispiel-Ablauf Conversational Prompting:**

> 1. "Welche Kampagnenansätze gibt es für ein lokales Restaurant, das jüngere Zielgruppen ansprechen will?"
> 2. *(KI liefert 5 Ansätze)* "Ansatz 3 gefällt mir. Entwickle den weiter. Fokus auf Instagram Reels."
> 3. *(KI vertieft)* "Gut, jetzt schreib mir 5 mögliche Headlines für die Kampagne."
> 4. *(KI liefert Headlines)* "Headline 2 und 4 sind gut. Kombiniere beide zu einer neuen."

> Du siehst: Schritt für Schritt. Du steuerst, die KI liefert. Explorativer Prozess.

### Single Shot Prompting (für produktive Anwendungsfälle)

> Wenn du GENAU weißt, wie das Ergebnis aussehen soll. Zum Beispiel: "Ich brauche einen Facebook-Post für das Oster-Special, in diesem Format, mit diesem Stil, mit diesen Infos."
>
> Dann schreibst du EINEN Prompt, der alles enthält, und bekommst auf Knopfdruck ein fertiges Ergebnis. Das ist der große Effizienz-Hebel. Einmal einen guten Prompt bauen, dann immer wieder verwenden.

**Wichtige Unterscheidung:**

| | Conversational | Single Shot |
|---|---|---|
| Wann? | Ergebnis unklar | Ergebnis klar |
| Wie? | Schrittweise, im Dialog | Ein Prompt, fertiges Ergebnis |
| Gut für | Brainstorming, Konzepte, Ideenfindung | Wiederkehrende Texte, standardisierte Formate |
| Effizienz | Weniger skalierbar | Sehr skalierbar, reproduzierbar |
| Beispiel Werbung | "Welche Kampagnenidee für Kunde X?" | "Schreib Facebook-Post nach Vorlage Y für Kunde X" |

> **Beide haben ihre Berechtigung.** Conversational für die Kreativphase, Single Shot für die Produktion. Im Alltag wirst du beides nutzen.

## Die Prompt-Bausteine im Detail (12 Min)

> Jetzt bauen wir gemeinsam einen Prompt auf. Baustein für Baustein. Ich erkläre jeden Baustein und wir füllen ihn zusammen aus.

**Am Bildschirm: Leeres Dokument/Chat öffnen, nach und nach befüllen.**

### Baustein 1: Rolle (Role Prompting)

> Der erste Baustein gibt dem Modell eine Identität. Nicht "Du bist ChatGPT", sondern eine Rolle mit der Kompetenz, die du für diese Aufgabe brauchst.

**Theresa tippt vor:**

```markdown
# Rolle
Du bist eine erfahrene Werbetexterin mit 15 Jahren Erfahrung
in einer Full-Service-Agentur in Österreich. Dein Schwerpunkt
ist Kampagnenkonzeption und Texterstellung für Print, Online
und Social Media. Du kennst die österreichische Mentalität und
schreibst Texte, die verkaufen, ohne aufdringlich zu sein.
```

> Warum so detailliert? Weil "Du bist ein Werbetexter" zu generisch ist. Je genauer du die Rolle beschreibst, desto besser trifft das Modell den Ton.

### Baustein 2: Kontext

> Hier gibst du dem Modell alles, was es wissen muss, um deine Situation zu verstehen. Setting the Scene, du kreierst das Bühnenbild.

```markdown
# Kontext
Du arbeitest an einem Auftrag für [Kundenname], ein
[Branche/Beschreibung] in [Ort]. Das Unternehmen
[Positionierung/Alleinstellungsmerkmal].

Die Zielgruppe ist [demografische + psychografische
Beschreibung].

Der Ton der Marke ist [Beschreibung der Markenstimme].
```

> **Michaela:** Denk an einen deiner aktuellen Kunden. Welche Infos würdest du hier reinschreiben?

*(Kurzer Austausch, Michaela nennt Infos, Theresa zeigt wie man sie strukturiert.)*

### Baustein 3: Aufgabenbeschreibung + Schritt für Schritt

> Hier sagst du GENAU, was das Modell tun soll. Und du gibst eine Schritt-für-Schritt-Anleitung, wie es vorgehen soll.

```markdown
# Aufgabe
Deine Aufgabe ist es, [konkretes Ergebnis] zu erstellen.

Gehe dabei wie folgt vor:
1. Starte mit [Schritt 1, z.B. einem starken Hook]
2. Dann [Schritt 2, z.B. die Key Message vermitteln]
3. Danach [Schritt 3, z.B. Social Proof einbauen]
4. Schließe mit [Schritt 4, z.B. Call-to-Action]
```

> Die Schritt-für-Schritt-Anleitung ist besonders wichtig. Du definierst damit die Reihenfolge und Struktur des Outputs. Das Modell folgt diesen Schritten.

### Baustein 4: Input/Inhalt

> Manchmal hast du spezifische Inhalte, die der Text enthalten MUSS. Briefing-Infos, Key Messages, Produktdetails. Die packst du hier rein und kennzeichnest sie klar.

```markdown
# Inhalt
Verwende ausschließlich folgende Informationen:
<inhalt>
- Produkt: Bio-Olivenöl "Terra Verde", 500ml, € 12,90
- Herkunft: Familienweingut in Kalabrien, 4. Generation
- USP: Kaltgepresst, ungefiltert, direkt vom Erzeuger
- Key Message: Echter Geschmack statt Massenware
- Aktion: -20% bis Ende April mit Code FRUEHLING
</inhalt>
```

> Die spitzen Klammern `<inhalt>` und `</inhalt>` helfen dem Modell, den Inhaltsblock klar vom Rest des Prompts zu trennen. Das verbessert die Ergebnisse.

### Baustein 5: Beispiele

> Das ist einer der mächtigsten Bausteine. Wenn du dem Modell zeigst, wie gute Ergebnisse aussehen, versteht es den gewünschten Stil viel besser als durch jede Beschreibung.

```markdown
# Beispiele
Hier sind Beispiele für den gewünschten Stil und das gewünschte
Format. Verwende denselben Stil, OHNE Inhalte der Beispiele zu
übernehmen.

<beispiele>
## Beispiel 1
[Einen bisherigen guten Post/Text des Kunden einfügen]

## Beispiel 2
[Einen weiteren guten Post/Text einfügen]
</beispiele>
```

> **Tipp:** Sammle dir für jeden Kunden 3-5 gute Texte als Beispiele. Die kannst du immer wieder verwenden.

### Baustein 6: Stil

> Hier beschreibst du, WIE der Text klingen soll. Das ist für Werbung besonders wichtig.

```markdown
# Stil
- Direkte Ansprache, Du-Form
- Aktive Sprache, kurze Sätze
- Warmherzig aber nicht kitschig
- Humor ja, Sarkasmus nein
- Bildhafte Sprache, die Appetit macht
- Klingt wie eine gute Freundin, die einen Tipp gibt,
  nicht wie eine Werbeanzeige
```

### Baustein 7: Format

> Wie soll der Output aussehen? Länge, Struktur, visuelle Elemente.

```markdown
# Format
- Max. 180 Wörter
- Starker erster Satz (Hook), max. 1 Zeile
- Kurze Absätze (2-3 Zeilen)
- 1-2 Emojis, dezent eingesetzt
- Call-to-Action als letzter Absatz
- Link am Ende
```

### Baustein 8: Anweisungen (Dos & Don'ts)

> Zum Schluss: Klare Regeln, was das Modell tun und was es NICHT tun soll.

```markdown
# Anweisungen
- Schreibe auf österreichischem Deutsch
- Verwende die Key Messages aus dem Inhalt, erfinde NICHTS dazu
- Kein "einzigartig", "unvergesslich", "exklusiv" oder andere
  abgenutzten Werbefloskeln
- KEIN "Lass dir das nicht entgehen"
- Nicht mehr als 2 Emojis
- Identifiziere dich mit dem Autor, schreibe in Ich/Wir-Form

# WICHTIG (Wiederholung der Kernpunkte)
Erstelle einen Facebook-Post im beschriebenen Stil.
Max. 180 Wörter. Keine generischen Floskeln.
Der Ton ist warmherzig und appetitanregend.
```

> Die letzte Sektion "WICHTIG" am Ende ist ein Trick gegen den Lost-in-the-Middle-Effekt. KI-Modelle verarbeiten den Anfang und das Ende eines Prompts besser als die Mitte. Deshalb wiederholst du die wichtigsten Punkte am Ende nochmal.

## Wichtige Praxis-Tipps (3 Min)

### 1. Immer neues Chatfenster

> Ganz wichtig: Für jeden neuen Prompt-Durchgang ein neues Chatfenster öffnen. Nicht im gleichen Chat weiterprompten. Warum? Weil der alte Chatverlauf das Ergebnis beeinflusst. Sauberer Start = saubereres Ergebnis.

### 2. Resampling

> Klick 3x auf "Erneut generieren". Weil KI probabilistisch arbeitet, bekommst du jedes Mal ein leicht anderes Ergebnis. Nimm das Beste.

### 3. Self Evaluation

> Lass die KI ihren eigenen Text bewerten. Sag: "Bewerte diesen Text anhand folgender Kriterien: [Kriterien]" oder erstelle vorher eine Checkliste und lass den Text dagegen prüfen. Das funktioniert erstaunlich gut.

### 4. Lost-in-the-Middle

> Bei langen Prompts: Wichtigstes an den Anfang. Wichtigstes am Ende wiederholen. Mittelteil in Stichpunkten statt Fließtext. Kritische Regeln mit WICHTIG, NICHT, IMMER, AUF KEINEN FALL markieren.

## Gemeinsam einen Prompt bauen (5 Min)

> Jetzt bist du dran. Denk an einen Text, den du diese Woche für einen Kunden schreiben musst. Wir bauen jetzt zusammen den Prompt dafür.

*(Theresa und Michaela gehen gemeinsam die Bausteine durch. Michaela liefert die Infos aus ihrem Arbeitsalltag, Theresa hilft beim Strukturieren. Der fertige Prompt wird in ChatGPT eingegeben.)*

**Überleitung:** *"Gut, jetzt hast du deinen ersten richtigen Prompt gebaut. Im letzten Block üben wir das nochmal mit einem konkreten Anwendungsfall aus deinem Alltag."*

---

---

# BLOCK 5: Michaelas Anwendungsfall -- Werbung (20 Min)

---

## Lernziel

Michaela erstellt eigenständig (mit Unterstützung) einen kompletten Prompt für einen realen Anwendungsfall aus ihrem Arbeitsalltag und sieht den iterativen Prozess in Aktion.

## Vorbereitung (2 Min)

**Theresa sagt sinngemäß:**

> Jetzt machen wir es richtig. Du nimmst dir einen konkreten Text, den du sowieso diese Woche schreiben musst, und wir bauen den Prompt dafür. So hast du am Ende nicht nur was gelernt, sondern auch was Fertiges.

**Michaela wählt einen Anwendungsfall:**

Mögliche Optionen (je nachdem was Michaela gerade auf dem Tisch hat):
- Werbetext für eine laufende Kampagne
- Social-Media-Post für einen Kunden
- Headlines/Slogans für ein Produkt
- Newsletter-Text
- Angebots- oder Präsentationstext
- Konzeptpapier/Briefing-Zusammenfassung

Falls Michaela nichts Konkretes hat, verwende dieses Szenario:

> **Fallback-Szenario:** Ein lokaler Wiener Blumenladen launcht einen Online-Shop. Michaela soll den Werbetext für die Startseite schreiben. Zielgruppe: Wienerinnen 30-55, die Wert auf Qualität und Regionalität legen. Tonalität: persönlich, nicht hipster, nicht steif.

## Übung Teil 1: Prompt gemeinsam bauen (8 Min)

Michaela diktiert, Theresa unterstützt bei der Strukturierung.

**Schritt für Schritt:**

1. **Rolle festlegen:** Welche Expertise brauchen wir? Welche Erfahrung?
2. **Kontext sammeln:** Was weiß Michaela über den Kunden? Zielgruppe? Marke? Tonalität?
3. **Aufgabe formulieren:** Was genau soll erstellt werden? In welchen Schritten?
4. **Inhalt einfügen:** Welche Fakten, Key Messages, Infos muss der Text enthalten?
5. **Beispiele:** Hat Michaela bisherige Texte des Kunden, die gut funktioniert haben?
6. **Stil beschreiben:** Wie soll es klingen?
7. **Format:** Länge, Struktur, visuelle Elemente?
8. **Anweisungen:** Was soll das Modell tun, was NICHT?
9. **WICHTIG am Ende:** Kernpunkte wiederholen

## Übung Teil 2: Prompt abschicken und bewerten (5 Min)

1. **Prompt in ChatGPT (oder Claude) eingeben**
2. **Ergebnis gemeinsam lesen und bewerten:**
   - Was ist gut?
   - Was klingt noch generisch?
   - Fehlt etwas?
   - Stimmt die Tonalität?
   - Würde Michaela das so an den Kunden schicken?

**Leitfragen für die Bewertung:**

| Frage | Check |
|---|---|
| Klingt es nach dem Kunden oder nach "irgendeinem" Unternehmen? | |
| Ist die Tonalität richtig? | |
| Sind alle Key Messages enthalten? | |
| Gibt es generische Floskeln, die raus müssen? | |
| Stimmt die Länge und das Format? | |
| Würdest du es so posten/senden? | |

## Übung Teil 3: Iterieren und verbessern (5 Min)

> Jetzt optimieren wir. Wir passen den Prompt an, basierend auf dem, was beim ersten Ergebnis nicht gepasst hat.

**Typische Anpassungen:**
- "Die Tonalität war zu förmlich" --> Stil-Sektion anpassen, mehr Beispiele für lockeren Ton
- "Es fehlte der Call-to-Action" --> In Aufgabe explizit als Schritt einfügen
- "Zu lang" --> Format-Sektion: "Max. X Wörter, kein Wort mehr"
- "Generische Floskeln" --> In Anweisungen explizit verbieten: "Verwende NIEMALS: [Floskel 1, Floskel 2, ...]"
- "Klingt nicht nach der Marke" --> Mehr/bessere Beispiele einfügen

**Zweiten Durchlauf starten:**
1. Angepassten Prompt in NEUEM Chatfenster eingeben
2. Ergebnis vergleichen: Ist es besser?
3. Optional: 3x "Erneut generieren" und bestes Ergebnis nehmen

> Siehst du den Unterschied? Mit jeder Iteration wird es besser. Und wenn der Prompt einmal steht, kannst du ihn für den nächsten Auftrag desselben Kunden wiederverwenden. Nur die Inhalte austauschen.

---

---

# ZUSAMMENFASSUNG & CHEAT SHEET (letzte Minuten)

---

## Die 5 wichtigsten Regeln für Michaela

1. **KI ist dein hochbegabter Praktikant** -- du musst ihn genau anweisen. Je besser dein Briefing, desto besser sein Output.

2. **Drei Prinzipien, immer alle drei:** Struktur (klar gegliedert), Spezifizität (genau beschreiben was du willst) und Kontext (alle Infos mitgeben, besonders Beispiele).

3. **Generisch ist der Feind.** Ohne guten Prompt kommt Durchschnitt raus. Dein Job: Durch spezifische Prompts überdurchschnittliche Ergebnisse herausholen.

4. **Ergebnisse IMMER prüfen.** KI halluziniert, generiert Mittelmaß, macht Fehler. Du bist der letzte Check.

5. **Iterieren.** Gute Ergebnisse kommen selten beim ersten Versuch. Prompt anpassen, neu generieren, vergleichen. 3x ist normal.

## Schnellstart-Tipps

- **Neues Chatfenster** für jeden neuen Prompt-Durchgang
- **Resampling:** 3x generieren, bestes nehmen
- **Beispiele sind Gold:** Für jeden Kunden 3-5 gute Referenztexte sammeln
- **ChatGPT** für Allround-Aufgaben und Recherche, **Claude** für Copywriting
- **Canvas** (ChatGPT) oder **Artifacts** (Claude) zum Feinschliff nutzen
- **Personalisierung** in ChatGPT einrichten: Wer du bist, was du machst

## Ausblick: GPTs -- der nächste Schritt

> Wenn du dich mit Prompting wohlfühlst, ist der nächste Schritt, dir eigene GPTs zu bauen. Das sind eigene ChatGPT-Versionen, die du einmal einrichtest und die sich dann immer gleich verhalten.
>
> Stell dir vor: Ein GPT "Social Media Posts für Kunde X", der schon die Markenstimme, die Zielgruppe, die Beispiele und den Stil kennt. Du gibst nur noch das Thema ein und bekommst einen fertigen Post.
>
> Bestandteile:
> - **Instructions:** Dein Prompt (Rolle, Kontext, Stil, Anweisungen)
> - **Knowledge Base:** Hochgeladene Dateien (Briefings, Beispiele, Markenleitfaden)
>
> Das können wir in einer nächsten Session machen, wenn du magst.

## Prompt-Vorlage zum Mitnehmen

*(Diese Vorlage Michaela als Datei schicken oder ausdrucken)*

```markdown
# Rolle
Du bist [Rolle + Beschreibung + Kompetenz].

# Kontext
Kunde: [Name, Branche, Positionierung]
Zielgruppe: [Demografie, Psychografie, Bedürfnisse]
Markenstimme: [Tonalität, Beispiele]

# Aufgabe
Deine Aufgabe ist es, [konkretes Ergebnis] zu erstellen.
Gehe dabei wie folgt vor:
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

# Inhalt
Verwende ausschließlich folgende Informationen:
<inhalt>
[Briefing, Produktinfos, Key Messages]
</inhalt>

# Beispiele
Erstelle den neuen Text im selben Stil wie diese Beispiele,
ohne deren Inhalte zu übernehmen:
<beispiele>
## Beispiel 1
[Referenztext 1]

## Beispiel 2
[Referenztext 2]
</beispiele>

# Stil
[Beschreibung des gewünschten Stils]

# Format
- Länge: [max. X Wörter]
- Struktur: [Absätze, Listen, etc.]
- Besonderheiten: [Emojis, Hashtags, Links, etc.]

# Anweisungen
- Achte darauf: [...]
- Vermeide: [...]
- Schreibe auf: [Sprache/Variante]

# WICHTIG (Wiederholung)
[Die 3 wichtigsten Punkte nochmal am Ende]
```

---

## Vorbereitung Theresa

### Material vorbereiten
- [ ] Laptop/Bildschirm für Live-Demo bereit
- [ ] ChatGPT-Account geöffnet (Plus oder Team)
- [ ] Claude-Account geöffnet (zum Vergleich zeigen)
- [ ] Überblicksgrafik (Bilder 1-15) als Präsentation/Slideshow vorbereiten
- [ ] Demo-Prompt Restaurant vorbereitet (Block 3, Kopie zum schnellen Einfügen)

### Für Michaela vorbereiten
- [ ] Prompt-Vorlage ausdrucken oder als Datei bereit
- [ ] Cheat Sheet (5 Regeln + Schnellstart-Tipps) ausdrucken
- [ ] Leeres Dokument vorbereiten für gemeinsamen Prompt-Bau (Block 4/5)

### Michaela vorher fragen
- [ ] "Bring bitte einen konkreten Textauftrag mit, den du gerade auf dem Tisch hast. Muss nichts Großes sein, ein Social-Media-Post reicht."
- [ ] "Hast du einen ChatGPT-Account? Falls ja, bring deinen Laptop mit."

### Nachbereitung
- [ ] Michaela die Prompt-Vorlage als Datei schicken
- [ ] Michaela die Überblicksgrafik schicken (Bilder als PDF)
- [ ] Anbieten: "Wenn du in den nächsten Wochen einen Prompt baust und nicht weiterkommst, schick ihn mir, ich geb dir Feedback."
- [ ] Optional: Termin für Follow-up anbieten (GPTs bauen)

---

*Erstellt: 2026-03-18*
*Basiert auf: KIPA-Ausbildungsinhalte (Garrit Wilson), Überblicksgrafik KI-Modelle*
*Referenz: `reference/ki-llms-wissensbasis.md`*
