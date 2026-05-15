import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", choices=["on", "off"])
args = parser.parse_args()
print(f"Lights {args.value}!")

