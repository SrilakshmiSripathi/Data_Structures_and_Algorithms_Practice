def finalValueAfterOperations(operations):
    X = int(0)
    for i in operations:
        print(eval(i))



operations = ["--X","X++","X++"]
finalValueAfterOperations(operations)
