def GuardsPos(TotalPaintings):
    GPosition = [0] * len(TotalPaintings)
    ArtsGuarded = {}
    pos = 0
    guards = 1
    while pos <= len(TotalPaintings):
        pos2 = pos + 1
        pos3 = pos + 2
##        print pos,i2,i3 ,'\t', len(TotalPaintings)
        if pos2 < len(TotalPaintings) and pos3 < len(TotalPaintings):
            GPosition[pos] = guards
            GPosition[pos2] = guards
            GPosition[pos3] = guards
            
        elif pos2 < len(TotalPaintings):
            GPosition[pos] = guards
            GPosition[pos2] = guards
        else:
            GPosition[pos] = guards
        guards += 1
        pos = pos + 3
##        print GPosition
    for i in GPosition:
        ArtsGuarded[i] = ArtsGuarded.get(i, 0)
    return 'Minimum number of guards required: ', len(ArtsGuarded)

NoOfPaintings = [1,4,5,7,9,11,13,15,16,19,20,21,22,24,25,65,77,76,90]
print GuardsPos(NoOfPaintings)
Gallery2 = [1,3,8,12,13]
print GuardsPos(Gallery2)
Gallery3 = [0,2,3,6,8,10,13]
print GuardsPos(Gallery3)
