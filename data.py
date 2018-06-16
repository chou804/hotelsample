import json
from pprint import pprint

data=[]
with open("hotel_C_f.json", "r", encoding="utf-8") as f:
    raw = json.load(f)
    # pprint(raw["XML_Head"]["Infos"]["Info"][0])
    for r in raw["XML_Head"]["Infos"]["Info"]:
        data.append(json.dumps(r ,ensure_ascii=False).encode('utf8').decode("utf-8"))

idCount = 1
with open('hotel_sample.json', 'w', encoding="utf-8") as fp:
    # ",".join(myList )
    for d in data:
        fp.write('{"index":{"_id":"'+str(idCount)+'"}}')
        fp.write("\n")
        fp.write(d)
        fp.write("\n")
        idCount = idCount + 1

