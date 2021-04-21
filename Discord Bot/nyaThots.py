import json
import os

with open(f"./assets/text.json", "r") as f:
    dicto = json.load(f)
    for fileName in os.listdir("./thots/"):
        try: 
            tmp = dicto[fileName]
        except:
            print(fileName)
            dicto[fileName] = fileName[:-4]
            with open(f"./assets/text.json", "w") as v:
                json.dump(dicto, v, sort_keys=True, indent=4)