from src.extract import Extract
from src.load import Load
from src.transform import Transform

def main():
    ext = Extract()
    data = ext.pnadc(variavel=4099, estado=26)

    # ld = Load()
    # ld.load_json("pnadc", data)

    # ld.load_mongo(data[0], "IBGE", "PNADC")

    transformer = Transform()
    data = transformer.transform_pnadc()

    ld = Load()
    ld.load_sqlite(df = data)


if __name__ == "__main__":
    main()