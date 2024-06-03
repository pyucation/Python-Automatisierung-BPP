"""
Aufgabe: Schreibe eine Art "Setup-Skript", welches dir einen neuen Ordner "my-project" erstellt
und dort lokal die Python-Version 3.9.6 nutzt. Installiere die Module numpy und pandas
anschließend in dieser Version.
Nutze die gegebene Funktion "run_command", welche eine Liste erwartet. Bsp.:
>>> run_command(["cd", "testfolder"])
führt den command
>>> cd testfolder
aus.
"""
import os
import sys
import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()


if __name__ == "__main__":
    ...
