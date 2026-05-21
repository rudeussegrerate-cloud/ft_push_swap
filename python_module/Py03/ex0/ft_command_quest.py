
import sys

if __name__ == "__main__":
    i = 0
    print("=== Command Quest ===")
    if (len(sys.argv) < 2):
        print(f"Program name: {sys.argv[i]}")
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {sys.argv[i]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {i}")
