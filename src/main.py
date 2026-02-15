from game import *

if __name__ == '__main__':
    rule = CArule([4], [1], 5, von_neighbourhood)
    c = CAGame(50, rule, light_teme=False)
    while True:
        c.play()
        choice = input("Play Again? y/n\n")
        if choice.lower() == 'n':
            break