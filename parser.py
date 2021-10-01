import json, os

def load_monsters():
  results = {}
  for root, dirs, files in os.walk("jsons", topdown=False):
    for file in files:
      dat = json.loads(str(open("jsons/"+file, "r").read()))
      results[dat["name"]] = dat
  return results

if __name__ == "__main__":
  print(load_monsters())
