from classifications.gics import GICS
from stocks import IE00BK5BQT80 as all_world

if __name__ == "__main__":
    g = GICS()
    # i = ICB()
    g.createSchemaDefinitions()

    # all_world.showPie()
    print("script completed")
