from random import randint

cardFile = open("cards.txt", "r")
cards = []
excludedHandsIndex = set()

#create a procedure that eliminates the cards already dealt and is called with different number of parameters 
def excludeCards(*indices):
    for x in indices:
        # (docstring removed; it wasn't a comment)
        
        if x is None:
            continue
        if isinstance(x, (list, tuple, set)):
            for i in x:
                if i is not None:
                    excludedHandsIndex.add(i)
        else:
            excludedHandsIndex.add(x)
         

class HandDealt:
    def __init__(self, indexCard1=None, indexCard2=None):
        if indexCard1 is None or indexCard2 is None:
            self.dealcard()  # auto-deal on create
        else:
            self.indexCard1 = indexCard1
            self.indexCard2 = indexCard2
    

    #generate two indexes that show one hand and use excludeCards to not deal them again 
    def dealcard(self):
        # pick two different indices in [0, 51]
        self.indexCard1 = randint(0, 51)
        self.indexCard2 = randint(0, 51)
        while self.indexCard1 == self.indexCard2 or self.indexCard1 in excludedHandsIndex or self.indexCard2 in excludedHandsIndex:
            self.indexCard1 = randint(0, 51)
            self.indexCard2 = randint(0, 51)
        excludeCards(self.indexCard1, self.indexCard2)


#create a flop 
class seeFlop():
    def __init__(self, flopindex1 = None, flopindex2 = None, flopindex3 = None):
        if flopindex1 is None or flopindex2 is None or flopindex3 is None:
            self.dealflop()
        else:
            self.flopindex1 = flopindex1
            self.flopindex2 = flopindex2
            self.flopindex3 = flopindex3

    def dealflop(self):
        self.flopindex1 = randint(0,51)
        self.flopindex2 = randint(0,51)
        self.flopindex3 = randint(0,51)
        while (self.flopindex1 == self.flopindex2 or 
               self.flopindex1 == self.flopindex3 or 
               self.flopindex2 == self.flopindex3 or 
               self. flopindex1 in excludedHandsIndex or 
               self.flopindex2 in excludedHandsIndex or 
               self.flopindex3 in excludedHandsIndex):
            self.flopindex1 = randint(0, 51)
            self.flopindex2 = randint(0, 51)
            self.flopindex3 = randint(0, 51)
        excludeCards(self.flopindex1, self.flopindex2, self.flopindex3)
        
# read cards.txt
line = cardFile.readline().strip()
while line != "":
    cards.append(line)
    line = cardFile.readline().strip()

hand1 = HandDealt()  #  create an instance; __init__ calls dealcard
hand2 = HandDealt() 
flop = seeFlop()

cardFile.close()

print(excludedHandsIndex, "excluded hands")
print(cards)
print(hand1.indexCard1, hand1.indexCard2, "first hand indexes")
print(hand2.indexCard1, hand2.indexCard2, "second hand indexes")
print(flop.flopindex1, flop.flopindex2, flop.flopindex3, "flop indexes")
print(cards[hand1.indexCard1], cards[hand1.indexCard2], "first hand")
print(cards[hand2.indexCard1], cards[hand2.indexCard2], "second hand")
print(cards[flop.flopindex1], cards[flop.flopindex2], cards[flop.flopindex3], "flop")