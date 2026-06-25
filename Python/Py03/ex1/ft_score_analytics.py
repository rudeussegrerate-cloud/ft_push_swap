import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    j = 0
    if (len(sys.argv) < 2):
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ..")
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
        print(f"Scores processed: {argscor}")
        print(f"Total players: {j}")
        print(f"Total score: {sum(argscor)}")
        print(f"Average score: {round(sum(argscor)/len(argscor), 1)}")
        print(f"High score: {max(argscor)}")
        print(f"Low score: {min(argscor)}")
        print(f"Score range: {max(argscor) - min(argscor)}")
    except Exception:
        print(f"Average score: {round(0, 1)}")
        print("High score: 0")
        print("Low score: 0")
        print("Score range: 0")
