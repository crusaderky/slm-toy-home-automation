import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", choices=["on", "off"])
args = parser.parse_args()
msg = f"DEMO API: Lights {args.value}!"
print(msg)
with open("lights", "w") as fh:
    fh.write(msg + "\n")

