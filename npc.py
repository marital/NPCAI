class Npc:
    def __init__(self, name):
        self._name = name
    
    def walk(self):
        pass

    def run(self):
        pass

    def escape(self):
        pass

    @property
    def name(self):
        return self._name

class Human(Npc):
    def talk(self, word):
        pass

class Man(Human):
    def walk(self):
        print("{}は歩いた".format(self._name))
        pass

    def talk(self, word):
        print("{}:{}".format(self.name,word))

    def run(self):
        pass

    def escape(self):
        pass
    
