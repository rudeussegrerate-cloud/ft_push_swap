#!/usr/bin/env python3
import sys
import typing


class Usage(Exception):
    def __init__(self,
                 Error: str = "Usage: ft_ancient_text.py <file>") -> None:
        super().__init__(Error)


if __name__ == "__main__":
    try:
        if (len(sys.argv) != 2):
            raise Usage()
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO[str] = open(sys.argv[1], "r",  encoding="utf-8")
        print("---")
        print(f.read())
        f.close()
        print("---")
        print(f"File '{sys.argv[1]}' closed")

    except Usage as e:
        print(e)
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
