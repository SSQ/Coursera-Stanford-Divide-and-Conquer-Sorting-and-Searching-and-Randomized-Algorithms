import random
import copy

with open('kargerMinCut.txt') as f:
    #kargerMinCut
    #a = [[int(x) for x in ln.split()] for ln in f]
    data_set = []
    for ln in f:
        line = ln.split()
        if line:
            a = [int(x) for x in line]
            data_set.append(a)

def choose_random_edge(data):
    a = random.randint(0,len(data)-1)
    b = random.randint(1,len(data[a])-1)
    return a,b

def compute_nodes(data):
    data_head = []
    for i in xrange(len(data)):
        data_head.append(data[i][0])
    return data_head

def find_index(data_head,data,u,v):
    index = data_head.index(data[u][v])
    return index

def replace(data_head,data,index,u):
    for i in data[index][1:]:
        index_index = data_head.index(i)
        for position,value in enumerate(data[index_index]):
            if value == data[index][0]:
                data[index_index][position] = data[u][0]
    return data
    
def merge(data):
    u,v = choose_random_edge(data)
    #print u,v
    data_head = compute_nodes(data)
    index = find_index(data_head,data,u,v)
    data[u].extend(data[index][1:])
    #print data
    data = replace(data_head,data,index,u)
    #print data
    data[u][1:] = [x for x in data[u][1:] if x!=data[u][0]]
    #print data
    data.remove(data[index])
    #print data
    return data

def KargerMinCut(data):
    
    data = copy.deepcopy(data)
    while len(data) >2:
        data = merge(data)
        #print data
    num = len(data[0][1:])
    return num

#KargerMinCut(data_set)
def calc_number(data,iteration):
    list = []
    for i in xrange(iteration):
        list.append(KargerMinCut(data))
    return min(list)



