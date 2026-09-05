#!/usr/bin/env python3
import sys
import typing


class Usage(Exception):
    def __init__(self,
                 Error: str = "Usage: ft_ancient_text.py <file>"):
        super().__init__(Error)


if __name__ == "__main__":
    try:
        if (len(sys.argv) != 2):
            raise Usage()
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file {sys.argv[1]}")

        f: typing.IO[str] = open(sys.argv[1], "r", encoding="utf-8")
        print("---")
        text = f.read()
        print(text)
        print(f"File '{sys.argv[1]}' closed")
        f.close()
        print("---")
        print("Transform data:")
        list_t = text.split('\n')
        print("---\n")

        for t in list_t:
            print(f"{t}#")

        print("\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().strip()
        fu: typing.IO[str] = open(file_name, "w", encoding="utf-8")
        print(f"Saving data to '{file_name}'")
        i = 0
        for t in list_t:
            i += 1
            if i < len(list_t):
                fu.write(f"{t}#\n")
            else:
                fu.write(f"{t}#")
        sys.stdout.write(f"Data saved in file '{file_name}'")
        fu.close()

    except Usage as e:
        sys.stderr.write(f"[STDERR] {e}\n")
    except (KeyboardInterrupt, EOFError):
        sys.stderr.write("\n[STDERR] Not saving data.\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
