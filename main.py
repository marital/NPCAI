from npc import Npc, Human, Man

if __name__ == "__main__":
    john = Man("john")
    choice = input("話しかける？yes or no\n")
    if(choice in "yes"):
        john.talk("おはよう")
        key = input()
        john.talk("調子はどうだい？")