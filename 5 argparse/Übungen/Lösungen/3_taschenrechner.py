"""
Aufgabe: Schreibe ein einfaches Taschenrechnerprogramm, welches die
vier Grundrechenarten (Addition, Subtraktion, Multiplikation und Division)
beherrscht. Die Funktionen sollen über die Kommandozeile aufrufbar sein.
Verwende argparse und 'positional arguments', um das zu realisieren.
Hinweis: Nutze 'mutually exclusive arguments'!
"""
import argparse


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # optional, aber sinnvoll!
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Einfacher Taschenrechner")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", nargs=2,
                       type=float, help="Addiere zwei Zahlen")
    group.add_argument("-s", "--subtract", nargs=2, type=float,
                       help="Subtrahiere zwei Zahlen")
    group.add_argument("-m", "--multiply", nargs=2, type=float,
                        help="Multipliziere zwei Zahlen")
    group.add_argument("-d", "--divide", nargs=2, type=float,
                        help="Dividiere zwei Zahlen")

    args = parser.parse_args()

    if args.add:
        result = add(args.add[0], args.add[1])
    elif args.subtract:
        result = subtract(args.subtract[0], args.subtract[1])
    elif args.multiply:
        result = multiply(args.multiply[0], args.multiply[1])
    elif args.divide:
        result = divide(args.divide[0], args.divide[1])

    print("Ergebnis:", result)
