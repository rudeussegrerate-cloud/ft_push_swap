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

        f: typing.IO[str] = open(sys.argv[1], "r")
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
            if t:
                print(f"{t}#")
        print("\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().strip()
        fu: typing.IO[str] = open(file_name, "w")
        print(f"Saving data to '{file_name}'")
        for t in list_t:
            if t:
                fu.write(f"{t}#\n")
        sys.stdout.write(f"Data saved in file '{file_name}'")
        fu.close()

    except Usage as e:
        sys.stderr.write(f"[STDERR] {e}")
    except KeyboardInterrupt:
        sys.stderr.write("\n[STDERR] Not saving data.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")
