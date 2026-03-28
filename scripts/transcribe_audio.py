"""
Audio-Transkription mit OpenAI Whisper

Transkribiert Audiodateien (m4a, ogg, mp3, wav) mit OpenAI Whisper
und speichert das Ergebnis als JSON und Markdown.

Verwendung:
    python scripts/transcribe_audio.py <audiodatei_oder_ordner>

Beispiel:
    python scripts/transcribe_audio.py "Wie KI Modelle funktionieren/Neue Aufnahme 5.m4a"
    python scripts/transcribe_audio.py "Wie KI Modelle funktionieren"
"""

import sys
import os
import subprocess
import json
from pathlib import Path

# --- Konfiguration ---
WHISPER_MODEL = "medium"
LANGUAGE = "de"
FFMPEG_PATH = "ffmpeg"
SUPPORTED_FORMATS = {".m4a", ".ogg", ".mp3", ".wav", ".webm", ".flac"}


def convert_to_mp3(input_path, mp3_path):
    """Konvertiert eine Audiodatei zu MP3."""
    cmd = [
        FFMPEG_PATH, "-i", str(input_path),
        "-codec:a", "libmp3lame", "-qscale:a", "2",
        "-y",
        str(mp3_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  FEHLER bei Konvertierung: {result.stderr[:200]}")
        return False
    return True


def transcribe_audio(audio_path, json_path, md_path, model, language):
    """Transkribiert eine Audiodatei mit Whisper und speichert als JSON + Markdown."""
    import whisper

    if not hasattr(transcribe_audio, "_model"):
        print(f"\nLade Whisper-Modell '{model}' (einmalig, kann dauern)...")
        transcribe_audio._model = whisper.load_model(model)

    result = transcribe_audio._model.transcribe(
        str(audio_path),
        language=language,
        verbose=False
    )

    output = {
        "datei": audio_path.stem,
        "sprache": result.get("language", language),
        "text": result["text"].strip(),
        "segmente": [
            {
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"].strip()
            }
            for seg in result["segments"]
        ]
    }

    # JSON speichern
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Markdown speichern
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Transkription: {audio_path.stem}\n\n")
        f.write(f"> Quelle: {audio_path.name} | Sprache: {output['sprache']} | Modell: {model}\n\n")
        f.write("---\n\n")
        f.write(output["text"])
        f.write("\n")

    return output["text"]


def process_file(audio_file, output_dir):
    """Verarbeitet eine einzelne Audiodatei."""
    name = audio_file.stem
    mp3_path = output_dir / f"{name}.mp3"
    json_path = output_dir / f"{name}.json"
    md_path = output_dir / f"{name}.md"

    print(f"\n  Datei: {audio_file.name}")

    if json_path.exists():
        print(f"  OK: Bereits transkribiert, überspringe.")
        return True

    # Schritt 1: Zu MP3 konvertieren (falls nicht schon mp3)
    if audio_file.suffix.lower() != ".mp3":
        if not mp3_path.exists():
            print(f"  Konvertiere {audio_file.suffix} -> MP3...")
            if not convert_to_mp3(audio_file, mp3_path):
                return False
        source = mp3_path
    else:
        source = audio_file

    # Schritt 2: Transkribieren
    print(f"  Transkribiere...")
    try:
        text = transcribe_audio(source, json_path, md_path, WHISPER_MODEL, LANGUAGE)
        preview = text[:100] + "..." if len(text) > 100 else text
        print(f"  OK: {preview}")
        return True
    except Exception as e:
        print(f"  FEHLER bei Transkription: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Verwendung: python scripts/transcribe_audio.py <audiodatei_oder_ordner>")
        sys.exit(1)

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Nicht gefunden: {target}")
        sys.exit(1)

    print(f"Modell: {WHISPER_MODEL} | Sprache: {LANGUAGE}")
    print("-" * 60)

    if target.is_file():
        if target.suffix.lower() not in SUPPORTED_FORMATS:
            print(f"Nicht unterstütztes Format: {target.suffix}")
            sys.exit(1)
        output_dir = target.parent
        output_dir.mkdir(exist_ok=True)
        success = process_file(target, output_dir)
        print("\n" + "=" * 60)
        print("Fertig!" if success else "Fehlgeschlagen!")
    else:
        # Ordner: alle Audiodateien verarbeiten
        audio_files = sorted(
            f for f in target.iterdir()
            if f.suffix.lower() in SUPPORTED_FORMATS
        )
        if not audio_files:
            print(f"Keine Audiodateien in {target} gefunden.")
            sys.exit(1)

        output_dir = target
        print(f"Gefunden: {len(audio_files)} Audiodateien in {target}")

        erfolg = 0
        fehler = 0
        for i, audio_file in enumerate(audio_files, 1):
            print(f"\n[{i}/{len(audio_files)}]")
            if process_file(audio_file, output_dir):
                erfolg += 1
            else:
                fehler += 1

        print("\n" + "=" * 60)
        print(f"Fertig! {erfolg} erfolgreich, {fehler} Fehler")


if __name__ == "__main__":
    main()
