import sys
import typing

class Usage(Exception):
    def __init__(self, Error="Usage: ft_ancient_text.py <file>"):
        super().__init__(Error)

def text_gen(f: typing.IO[str]) -> None:
        f.read(1)
        

if __name__ == "__main__":
    try:
        if (len(sys.argv) != 2):
            raise Usage()
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {sys.argv[1]}")
        try:
            f = open(sys.argv[1], "w")
            # text_gen(f)
            # f.close()
            # print(f"File '{sys.argv[1]}' closed")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")

    except Usage as e:
        print(e)