# Py 2.7 Crazy 8 Algorithm

import random


class Crazy8():
    def __init__(self, cSeq):
        self.cards = cSeq
        self.trickSeq = [0] * len(cSeq)
        self.prevCard = [None] * len(cSeq)

    def matchCards(self, card1, card2):
        """ Checks 2 input cards if they belong
            to same suit or same rank or has
            jack 8 card """

        card1Rank = card1[0]
        card2Rank = card2[0]
        card1Suit = card1[1]
        card2Suit = card2[1]

        if card1Rank == card2Rank:
            return True
        if card1Suit == card2Suit:
            return True
        if card1Rank == 8 or card2Rank == 8:
            return True
        return False

    def findTrickSequence(self):
        """ """
        # trickSeq, prevCard help keep book keeping of
        # best trick sequence and parent card
        self.trickSeq[0] = 1
        self.prevCard[0] = 0
        MaxIndex = 0

        # i loop to check all cards
        for i in range(len(self.trickSeq)):
            currMax = 0

            # j loop to check all previous cards
            for j in range(i):
                if self.trickSeq[j] > currMax:
                    if self.matchCards(self.cards[i], self.cards[j]):
                        currMax = self.trickSeq[j]
                        self.trickSeq[i] = currMax + 1
                        self.prevCard[i] = j

        if self.trickSeq[i] > self.trickSeq[MaxIndex]:
            MaxIndex = i
        # in trick we parse our booking keeping arrays to
        # get the trick sequence
        Trick = {}
        curPrev = MaxIndex
        for i in range(MaxIndex - 1, 0, -1):
            Trick[i] = self.cards[curPrev]
            curPrev = self.prevCard[curPrev]
        return self.printTrickSeqeunce(Trick)

    def printTrickSeqeunce(self, tricks):
        print "The length of trick sequence is", len(tricks)
        print "Trick Sequence", [i for i in tricks.values()]


def main():
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
    suits = ["C", "S", "H", "D"]
    seqLength = 6
    cntCards = len(ranks) - 1
    cntSuite = len(suits) - 1

    RandomCardSeq = {}
    for i in range(seqLength):
        # generate random cards
        ranR = random.randint(0, cntCards)
        ranS = random.randint(0, cntSuite)
        RandomCardSeq.update({(ranks[ranR] + suits[ranS]): 0})
    cardSeq = sorted(list(RandomCardSeq))
    #  Print card cardSeq
    print cardSeq
    # Create Card Sequence
    crazy8Seq = Crazy8(cardSeq)
    crazy8Seq.findTrickSequence()
main()
