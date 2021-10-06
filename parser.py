import json, os, glob

def load_monsters():
  files = [f for f in os.listdir(os.getcwd()) if f.endswith('.json')]
  print("const monsters = [")
  for f in files:
    with open(f) as file:
      print(file.read() + ",")
  print("]")

if __name__ == "__main__":
  load_monsters()
