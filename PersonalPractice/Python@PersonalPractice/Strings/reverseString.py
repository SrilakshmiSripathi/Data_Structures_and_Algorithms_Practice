#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    reversedString = ""
    
    newSentence = sentence[::-1].split(" ")
    
    for i in newSentence:
        newi = i[::-1]

        for j in newi:
            
            if j.isupper():
                reversedString += j.lower()
            elif j.islower():
                reversedString += j.upper()
            else:
                # if the string contains number or symbol, adding as it is
                reversedString += j
        reversedString +=  " "
    return reversedString
         
sentense = "aWESOME is cODING"
print(reverse_words_order_and_swap_cases(sentense))
