# Double Hashing
import math
import random
import FindNextPrime


class Hash():
    def __init__(self, keys, TabSize):
        # Constructor for keeping track of hash table,
        # and random genereted keys
        self.keys = keys
        self.tab = TabSize
        self.dhTab = [None] * TabSize
        self.LHTab = [None] * TabSize

    # Define Hashing
    def DoubleHashing(self):
        for key in self.keys:
            loc = key % self.tab
            if self.dhTab[loc] is None:
                self.dhTab[loc] = key
            elif self.dhTab[loc] is key:
                pass
            else:
                # When collision occurs
                currloc = loc
                while self.dhTab[currloc] is not None:
                    # computer second hash value to jump from current location
                    n = currloc + self.SecondHash(key)
                    if n < len(self.dhTab):
                        currloc = n
                    else:
                        currloc = n - len(self.dhTab)
                if self.dhTab[currloc] is None:
                    self.dhTab[currloc] = key
        return self.dhTab

    def SecondHash(self, key):
        return max(1, abs(5 - (key % self.tab)))

    def LinearProbing(self, ):
        for key in self.keys:
            # Hash function
            loc = key % self.tab
            if self.LHTab[loc] is None:
                self.LHTab[loc] = key
            elif self.LHTab[loc] is key:
                pass
            else:
                # if collision occurs
                currloc = loc
                while self.LHTab[currloc] is not None:
                    n = currloc + self.LinearCollision()
                    if n < len(self.LHTab):
                        currloc = n
                    else:
                        currloc = n - len(self.LHTab)
                if self.LHTab[currloc] is None:
                    self.LHTab[currloc] = key
        return self.LHTab

    def LinearCollision(self):
        # return index position to add for linear hash function
        return 1

    def Search(self, tab, AVN, kfrom, kto):
        """ shp is search hits probing count,
            smp is search miss probing count"""
        shp = 0
        smp = 0
        # To perform search operation on an average num_of_times(AVN)
        for i in range(AVN):
            shp += self.searchHit(tab, kfrom, kto)
            smp += self.searchMiss(tab, kto, 10 * kto)
        return shp/AVN, smp/AVN

    def searchHit(self, tab, l, r):
        probes, hits = 0, 0
        # Randomly generate a number and perform search hits in hash table
        check = random.randint(l, r)
        i = 0
        while i < len(tab)-1:
            probes += 1
            if tab[i] is check:
                hits += 1
                return probes
            else:
                i += 1
        return probes/hits

    def searchMiss(self, tab, l, r):
        probes, miss = 0, 0
        # Randomly generate a number and perform search miss in hash table
        check = random.randint(l, r)
        i = 0
        while i < len(tab)-1:
            if tab[i] is not check:
                probes += 1
                miss += 1
            i += 1
        return probes/miss


def main():
    LoadFactor = [0.5, 0.6666, 0.75, 0.9, 0.99]
    inputSize = 500
    print("inputSize", inputSize)
    # Calculated next desired prime number
    TabSize = FindNextPrime.primes(inputSize)
    keysFrom = 0
    keysTo = 2 * TabSize
    print ("Selected table size", TabSize)

    for loads in LoadFactor:
        print ("Load Factor", loads)
        Num_Keys_tab = int(math.ceil(loads * float(TabSize)))
        print ("Data in hash table", Num_Keys_tab)
        # Generete random keys
        randKeys = []
        for i in range(Num_Keys_tab):
            randKeys.append(random.randint(keysFrom, keysTo))
        newHash = Hash(randKeys, TabSize)

        # Hash random keys to hash table using Double hashing
        DHT = newHash.DoubleHashing()
        # Number of times to perform search operation
        searchTimes = 2 * Num_Keys_tab
        print ("\t Double Hashing:", "\n",
               newHash.Search(DHT, searchTimes, keysFrom, keysTo))
        # Hash random keys to hash table using Linear Probing
        LHT = newHash.LinearProbing()
        print ("\t Linear Probing:", "\n",
               newHash.Search(LHT, searchTimes, keysFrom, keysTo))
main()
