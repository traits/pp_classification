from classifications.gics import GICS
from stocks import IE00BK5BQT80 as all_world

if __name__ == "__main__":
    import xmltodict
    import json

    with open("../dkb.xml", "r", encoding="utf-8") as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert
    # the XML document
    my_dict = xmltodict.parse(my_xml)
    d = my_dict  # ["client"]["taxonomies"]
    with open("xxx.json", "w") as file:
        json.dump(d, file, indent=2)

    exit(0)

    g = GICS()
    # i = ICB()
    g.createSchemaDefinitions()

    # all_world.showPie()
    print("script completed")
