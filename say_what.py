def say_what():
    word = input("What word? ")
    times = int(input("How many times?"))
    for i in range(0,times):
        print(str(i + 1) + ".) " + word)
say_what()
