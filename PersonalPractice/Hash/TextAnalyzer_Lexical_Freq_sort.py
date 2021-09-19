import re
import heapq

class TextAnalyzer:
    def Hash(self, data):
        """Input: Tokenized string
            Ouput: Hash map"""
        wc_hash = {}
        for words in data:
            wc_hash[words] = wc_hash.get(words, 0) + 1
        return wc_hash
    
    def wordCount(self, para):
        """Input: Tokenized string
            Ouput: number of elements in hash map"""
        return len(self.Hash(para))

    def FreqSort(self, para):
        """Input: Tokenized String
            Output: Frequency of words in a paragraph
            Runtime: """
        # Hashing input paragraph Using wordCount method
        newdict = self.Hash(para)
        # HeapSorting by inserting key,value pair to heap
        newheap = []
        for value, key in newdict.items():
            heapq.heappush(newheap, (key, value))
        heapq.heapify(newheap)
        
        # Popping min_key from heap gives FreqOrder from 1-n
        
        for i in range(len(newheap)):
            k, v = heapq.heappop(newheap)
            print "-->", k,v
    
    def LexiSort(self, para):
        """Input: Tokenized String
            Output: Lexical order of words in a paragraph """

        # Hashing input paragraph Using wordCount method
        newdict = self.Hash(para)
        
        # HeapSorting by inserting value,key pair to heap
        newheap = []
        for i in newdict:
            heapq.heappush(newheap, i)
        heapq.heapify(newheap)

        # Popping min_value from heap gives lexiOrder(A-a-1)
        for i in range(len(newheap)):
            least = heapq.heappop(newheap)
            if least in newdict:
                print "-->", least,newdict[least]
                           
def main():
    # Read Paragraph from file
    f = open('input.txt', 'r')
    p = ''
    # Iterating thru file f to Concatenate into one string
    # Library re helps to tokenize the string to recognize words in the text
    for line in f:
        p = p + (line)
    data = re.findall(r'(?![0-9])\w+', p)
    # Create object to access class.
    txtA = TextAnalyzer()
    print ("Number of words found = ", txtA.wordCount(data))
    print ("Word and frequencies sorted by word frequencies")
    txtA.FreqSort(data)
    print ("Word and frequencies sorted lexicographically by words");
    txtA.LexiSort(data)
main()
