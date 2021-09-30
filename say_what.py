def say_what():
    word = raw_input("What word? ")
    times = input("How many times?")
    for i in range(0,times):
        print(str(i + 1) + ".) " + word)
say_what()
