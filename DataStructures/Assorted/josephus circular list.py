def josephus(n, k):
    circle = list(range(1, n + 1))
    circle[n - 1] = 0
    persons = 0
    winner = []
    while circle[persons] != persons:
        for i in range(k):
            print(i)
            persons = circle[persons]
        winner.append(circle[persons])
        circle[persons] = circle[circle[persons]]
        persons = circle[persons]
    winner.append(persons)
    return winner
 
#print (josephus(10, 4))
# k = 2 [1, 3, 5, 7, 9, 2, 6, 0, 8, 4]
# k = 4 [3, 7, 1, 6, 2, 9, 8, 0, 5, 4]
 
#print (josephus(41, 3))
30

print(josephus(5, 2))
