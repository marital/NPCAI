from random import choice
import re

class Responder:
    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary
    
    def response(self, *args):
        pass

    @property
    def name(self):
        return self._name

class WhatResponder(Responder):
    def response(self, text):
        return "{}ってなに?".format(text)

class RandomResponder(Responder):
    def __init__(self, name, dictionary):
        super().__init__(name, dictionary)
        self._responses = []
        with open('dics/random.txt', encoding = 'utf-8')as f:
            self._responses = [x for x in f.read().splitlines() if x]

    def response(self, _):
        return choice(self._responses)

class PatternResponder(Responder):
    def response(self, text):
        for ptn in self._dictionary.pattern:
            macher = re.match(ptn['pattern'],text)
            if macher:
                chosen_response = choice(ptn['phrases'])
                return chosen_response.replace('%match%',macher[0])
        return choice(self._dictionary.random)
