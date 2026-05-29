import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) < 3):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..")
    else:
        i = 1
        j = 0
        # print("Scores processed: [", end="")
        # while(i < len(sys.argv)):
        #     print(sys.argv[i], end="")
        #     if (i < len(sys.argv)-1):
        #         print(", ", end="")
        #     i+=1
        # print("]")
        arg = [0] * (len(sys.argv) - i)
        while (i < len(sys.argv)):
            try:
                arg[j] = int(sys.argv[i])
                j+=1
            except:
                print(f"invalid parameter: '{sys.argv[i]}'")
            i = i + 1
        if (not (arg[0] and arg[1])):
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..")
        else:
            i = 0
            argscor = [0] * j
            while(i < j):
                argscor[i] = arg[i]
                i+=1
            print(f"Scores processed: {argscor}")
            print(f"Total players: {j}\nTotal score: {sum(argscor)}\nAverage score: {sum(argscor)/len(argscor)}")
            print(f"High score: {max(argscor)}\nLow score: {min(argscor)}\nScore range: {max(argscor) - min(argscor)}")
