import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--verbosity",
                    help="Zeig mir MEHR")

args = parser.parse_args()

print("Hello World")
if args.verbosity:
    print("Even more hello world :)")

# kein Fehler, wenn nicht übergeben!
# man muss einen Wert angeben (irgendeinen)

# ---------------

# parser.add_argument("--verbosity",
#                     help="Zeig mir MEHR",
#                     action="store_true")

# args = parser.parse_args()

# print("Hello World")
# if args.verbosity:
#     print("Even more hello world :)")

# wenn wir jetzt einen Wert mitgeben, kommt eine Fehlermeldung
# stattdessen, durch action="store_true" haben wir ein echtes
# "Flag" gebaut!

# ----------------

# short options hinzufügen
# parser.add_argument("-v", "--verbosity",
#                     help="Zeig mir MEHR",
#                     action="store_true")

# args = parser.parse_args()

# print("Hello World")
# if args.verbosity:
#     print("Even more hello world :)")
