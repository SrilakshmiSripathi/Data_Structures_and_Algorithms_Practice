import re


def genGraph(k):
    """Input: Takes a .gr file
        Ouput: Generates a weighted edgeList for the graph"""
    Graph = {}
    # try reading file, to check for from_vertex,to_vertex, and weight values
    try:
        for line in k:
            if re.findall(r'c', line):
                pass
            elif re.findall(r'p \w+', line):
                v = re.findall(r'\w+', line)
                # vertex and edge counts, here v is a list [p, sp, vc, ec]
                vc = int(v[2])
                print 'Total Vertices', vc
                ec = int(v[3])
                print 'Total Edges', ec
            elif re.findall(r'a\s\w+', line):
                units = re.findall(r'\w+', line)
                u = int(units[1])
                v = int(units[2])
                w = int(units[3])
                if (u, v) not in Graph:
                    Graph.update({(u, v): w})
            else:
                print ("Found an illegal code")
    # Closes any open file thread to avoid I/O Error
    finally:
        k.close()
    return Graph


# Test graph module
def test():
    with open('rome99.gr', 'r') as ff:
        print genGraph(ff)
    ff.close()
    with open('graph01.gr', 'r') as fff:
        print genGraph(fff)
    fff.close()
