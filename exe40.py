Amma=[(1,3,2),(4,8,5),(7,9,4)]
print sorted(Amma,key=lambda tup:(tup[1],tup[2]))


data = [(1,2,3),(1,2,1),(1,1,4)]
print sorted(data, key=lambda tup: (tup[1],tup[2]) )
