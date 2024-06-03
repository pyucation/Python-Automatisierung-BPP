"""
Aufgabe:

    1. Daten einlesen:
        Lies die Log-Daten aus der CSV-Datei mit Pandas ein. (cybersecurity_logs.csv)

    2. Daten vorverarbeiten:
        Konvertiere die timestamp-Spalte in das Datetime-Format.
        Gruppiere die Daten nach event_type und berechne die Gesamtzahl der packet_count für jeden Ereignistyp.

    3. Daten analysieren:
        Finde heraus, welche IP-Adresse die meisten Ereignisse ausgelöst hat.
        Bestimme den Zeitraum mit der höchsten Anzahl an Paketen.

    4. Daten visualisieren:
        Erstelle ein Liniendiagramm, das die Anzahl der Pakete pro Zeitstempel für jeden Ereignistyp zeigt.
        Erstellee ein Balkendiagramm, das die Gesamtzahl der Pakete für jeden Ereignistyp darstellt.
        Erstelle ein Kreisdiagramm, das den Anteil der verschiedenen Ereignistypen an der Gesamtanzahl der Pakete zeigt.

Hinweis: Die folgenden Funktionen könnten hilfreich sein:
- reset_index() (zusammen mit groupby)
- idxmax()
- unique()
- im Zusammenhang mit groupby kann man dieser Funktion ein pd.Grouper-Objekt übergeben,
dieses eignet sich hervorragend zur Verwendung von timestamp/datetime-Daten (hier gerne in die Lösung
schauen, wer nicht weiterkommt, das ist nicht trivial)    
"""
import pandas as pd
import matplotlib.pyplot as plt


# Daten einlesen
logs = pd.read_csv('Datenverarbeitung-Gesamtübungen/cybersecurity_logs.csv')

# Daten vorverarbeiten
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
logs_grouped = logs.groupby('event_type')['packet_count'].sum().reset_index()

# Analyse
most_active_ip = logs['source_ip'].value_counts().idxmax()
busiest_period = logs.groupby(pd.Grouper(key='timestamp', freq='10Min'))['packet_count'].sum().idxmax()
# alternativ, wem das zu kompliziert ist, kann es auch so lösen:
grouped_logs = logs.set_index('timestamp').resample('10Min')['packet_count'].sum()
busiest_period = grouped_logs.idxmax()

print(f"Die IP-Adresse mit den meisten Ereignissen ist: {most_active_ip}")
print(f"Der Zeitraum mit der höchsten Anzahl an Paketen ist: {busiest_period}")

# Visualisierung
plt.figure(figsize=(14, 7))

# Liniendiagramm
for event_type in logs['event_type'].unique():
    subset = logs[logs['event_type'] == event_type]
    plt.plot(subset['timestamp'], subset['packet_count'], marker='o', label=event_type)

plt.title('Anzahl der Pakete pro Zeitstempel und Ereignistyp')
plt.xlabel('Zeitstempel')
plt.ylabel('Anzahl der Pakete')
plt.legend()
plt.show()

# Balkendiagramm
plt.figure(figsize=(10, 6))
plt.bar(logs_grouped['event_type'], logs_grouped['packet_count'], color=['blue', 'red'])
plt.title('Gesamtzahl der Pakete für jeden Ereignistyp')
plt.xlabel('Ereignistyp')
plt.ylabel('Gesamtzahl der Pakete')
plt.show()

# Kreisdiagramm
plt.figure(figsize=(8, 8))
plt.pie(logs_grouped['packet_count'], labels=logs_grouped['event_type'], colors=['blue', 'red'])
plt.title('Anteil der verschiedenen Ereignistypen an der Gesamtanzahl der Pakete')
plt.show()
