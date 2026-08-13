#!/usr/bin/env python3
import sys
import os
import site


if __name__ == "__main__":
    try:
        if sys.base_prefix == sys.prefix:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment!\n\
    The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env\n\
source matrix_env/bin/activate # On Unix\n\
matrix_env/Scripts/activate # On Windows\n\
Then run this program again.")

        else:
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!\n\
Safe to install packages without affecting\n\
the global system.\n")
            print(f"Package installation path:\n\
{site.getsitepackages()[0]}")
    except Exception as e:
        print(f"Got error: {e}")
