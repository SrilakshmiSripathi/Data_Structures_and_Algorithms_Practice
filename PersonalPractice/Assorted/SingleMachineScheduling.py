# Single Machine Scheduling

def TaskSch(Tasks):
    """Input: Tasks list
        Ouput: Single machine handling threads efficiently"""
    machine = []
    tast_time = 1
    for i in range(len(Tasks)):
        if Tasks[i][0] == tast_time:
            machine.append(Tasks[i])
            tast_time = Tasks[i][1]
    return machine

Tasks = [[1, 2], [1, 3], [1, 4], [2, 5], [3, 7], [4, 9], [5, 6],
         [6, 8], [7, 9]]
print TaskSch(Tasks)

Tasks = [[1, 3], [1, 5], [5, 6], [3, 7], [7, 9]]
print TaskSch(Tasks)
