# manchmal haben wir zwei Argumente, die sich gegenseitig ausschließend
import argparse

# siehe hier: Beschreibung, um Benutzer zu sagen, was wir
# hier überhaupt machen
parser = argparse.ArgumentParser(description="Rechne x hoch n")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# postional arguments
parser.add_argument("x", type=int, help="Basis")
parser.add_argument("n", type=int, help="Exponent")

args = parser.parse_args()
answer = args.x ** args.n

if args.quiet:
    # nur die Antwort
    print(answer)
elif args.verbose:
    # mit mehr Kontext
    print(f"{args.x} ^ {args.n} = {answer}")
    print("mehr Infos ...")
else:
    print(f"{args.x} ^ {args.n} = {answer}")
