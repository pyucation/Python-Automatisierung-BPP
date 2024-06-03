import argparse

parser = argparse.ArgumentParser()

# positionelles Argument mit dem Namen 'echo'
parser.add_argument("echo")
# parser.add_argument("echo", help="ein lautstarkes ECHOOO!")

# Rückgabewert abfangen
args = parser.parse_args()

print(f"The echo: {args.echo}")


# -------------------

# parser.add_argument("square", help="Quadriere diese Nummer")
# # parser.add_argument("square", help="Quadriere diese Nummer",
# #                     type=int)
# args = parser.parse_args()
# print(f"Quadiert: {args.square**2}")
