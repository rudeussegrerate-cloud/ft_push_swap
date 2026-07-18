#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    j = 0
    if (len(sys.argv) < 2):
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ..\n")
    else:
        arg = [0] * (len(sys.argv) - i)
        while (i < len(sys.argv)):
            try:
                arg[j] = int(sys.argv[i])
                j += 1
            except Exception:
                print(f"invalid parameter: '{sys.argv[i]}'")
            i = i + 1

        try:
            i = 0
            argscor = [0] * j
            while (i < j):
                argscor[i] = arg[i]
                i += 1
            if len(argscor) == 0:
                raise Exception()
            print(f"Scores processed: {argscor}")
            print(f"Total players: {j}")
            print(f"Total score: {sum(argscor)}")
            print(f"Average score: {sum(argscor)/len(argscor)}")
            print(f"High score: {max(argscor)}")
            print(f"Low score: {min(argscor)}")
            print(f"Score range: {max(argscor) - min(argscor)}\n")
        except Exception:
            print("No scores provided. Usage: python3 ", end="")
            print("ft_score_analytics.py <score1> <score2> ..\n")
