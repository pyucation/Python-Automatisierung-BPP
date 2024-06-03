"""
Aufgabe:
Installiere pyenv und dazu die Version 3.10.4.
Installiere anschließend die Module:
- numpy
- matplotlib
- pandas

Führe dann dieses Skript ohne Änderungen aus. Wenn es keine Fehler wirft, hast
du die Aufgabe erfolgreich erfüllt.
"""
import subprocess
import sys


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()


def check_pyenv_installed():
    try:
        run_command("pyenv --version")
    except Exception as e:
        print("pyenv is not installed. Please install pyenv first.")
        sys.exit(1)


def check_python_version():
    version = sys.version_info
    print(f"Current Python version: {version.major}.{version.minor}.{version.micro}")
    assert f"{version.major}.{version.minor}.{version.micro}" == "3.10.4",\
            "Wrong Python Version"
    

def check_modules():
    try:
        import numpy
        import pandas
        import matplotlib
    except Exception as e:
        print("one or more required modules is missing")
        print(f"terminated with error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    check_pyenv_installed()
    check_python_version()
    check_modules()

    print("Passed all tests! Task solved successfully!")
