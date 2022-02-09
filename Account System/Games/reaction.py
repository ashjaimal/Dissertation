import time, random

def reactionGame():
    print("WELCOME TO THE REACTION GAME")
    print("YOU SEE THE WORD GO HIT THE SPACEBAR")
    print("THE GAME WILL START IN 3 SECONDS")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

    time.sleep(random.randint(1,5))
    print("GO")
    tic = time.perf_counter()
    a = input()
    tock = time.perf_counter()

    totalTime = tock - tic
    print("--------------------------------------")
    print("YOUR TIME WAS: ", totalTime, "SECONDS" )

reactionGame()