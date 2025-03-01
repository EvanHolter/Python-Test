Words = ["Loops", "Cycles", "Iterations", "Generations"]

for i in range(len(Words)):
    print(i + 1, Words[i])

def main(help = False):
    action = int(input("How many time do you want main() to print? "))
    if help == True:
        print("main() is a function that prints")
    else:
        print("WHAT'S THE STORY MORNING GLORY " * action)

main()