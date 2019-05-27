from npc import Npc, Human, Man
from talkbot.unmo import Unmo

def build_prompt(unmo):
    return "{}:{}> ".format(unmo.name,unmo.responder_name)
    
if __name__ == "__main__":
    john = Man("john")
    choice = input("話しかける？yes or no\n")
    if(choice in "yes"):
        proto = Unmo("proto")
        while True:
            text = input("> ")
            if not text:
                break
        
            response = proto.dialog(text)
            print("{}{}".format(build_prompt(proto),response))