# jetzt kombinieren wir  beides
import argparse


parser = argparse.ArgumentParser()

# # positional argument (required!)
# parser.add_argument("quadrieren", type=int,
#                     help="Quadriere die gegebene Zahl")
# # optional argument
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="Zeig mehr an wenn gesetzt!")

# args = parser.parse_args()

# answer = args.quadrieren**2
# if args.verbose:
#     print(f"Quadrat von {args.quadrieren} = {answer}")
# else:
#     print(answer)

# --------------

# positional argument (required!)
parser.add_argument("quadrieren", type=int,
                    help="Quadriere die gegebene Zahl")
# optional argument, jetzt mit type int und kein Flag mehr!
# damit können wir bspw. verschiedene LEVEL angeben
parser.add_argument("-v", "--verbose", type=int,
                    help="Zeig mehr an wenn gesetzt!")
# um den Bug zu vermeiden (zeigt sich auch im --help):
# parser.add_argument("-v", "--verbose", type=int,
#                     choices=[0, 1, 2],
#                     help="Zeig mehr an wenn gesetzt!")

args = parser.parse_args()

answer = args.quadrieren**2
if args.verbose == 1:
    print(f"Quadrat von {args.quadrieren} = {answer}")
elif args.verbose == 2:
    print(f"Quadrat von {args.quadrieren} = {answer}")
    print(f"Und die Wurzel von {answer} ist folglich {args.quadrieren}")
else:
    print(answer)
