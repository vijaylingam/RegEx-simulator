__author__ = 'vijaychandra'

import networkx as nx
#import matplotlib.pyplot as plt
import itertools

graph = nx.DiGraph() # This only contains epislon trasitions
regexp = ""
#m = 0 #number of characters in regexp

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

def NFAwithEpsilon(regex):
    regexp = regex
    m = len(regex)
    ops = Stack()
    graph.add_nodes_from([i for i in range(m+1)]) # m+1 includes final state
    for i in range(m):
        lp = i
        if (regexp[i] == '(' or regexp[i] == '|'):
            ops.push(i)
        elif (regexp[i] == ')'):
            o = ops.pop()
            if regexp[o] == '|':
                lp = ops.pop()
                graph.add_edge(lp, o+1);
                graph.add_edge(o, i);
            elif regexp[o] == '(':
                lp = o
            else: assert False
        if(i < m-1 and regexp[i+1] == '*'):
            graph.add_edge(lp, i+1)
            graph.add_edge(i+1, lp)
        if (regexp[i] == '(' or regexp[i] == '*' or regexp[i] == ')'):
            graph.add_edge(i, i+1)
    if (ops.size() != 0):
        print("Invalid regular expression")
        return
    print("Epsilon Graph Edges List: ", graph.edges())

def evaluate(txt):

    dfs = list(nx.dfs_preorder_nodes(graph, 0))
    pc = [] #program counter
    for v in dfs:
        #if v >= 0 and v < m+1:
        pc.append(v)
    print("Epsilon states: ", set(pc))
    for i in range(len(txt)):
        if (txt[i] == '*' or txt[i] == '|' or txt[i] == '(' or txt[i] == ')'):
            print("text contains metacharacter '" + str(txt[i]) + "'")
            return
        match = []
        for v in set(pc):
            if (v == m): continue
            if ((reg[v] == txt[i] or reg[v] == '.')):
                match.append(v+1)
        print("Match states: ", set(match))
        new = []
        for i in match:
            x = []
            if (graph.degree(i)> 0):
                x = (list(nx.dfs_postorder_nodes(graph, i)))
                new.append(x)
            else:
                x.append(i)
            new.append(x)              
        dfs = list(itertools.chain.from_iterable(new))
        pc = []
        for v in range(len(dfs)):
            #if (dfs[v] >= 0 and dfs[v] < m+1): 
            pc.append(dfs[v])
        print("Epsilon states: ", set(pc))
        if (len(pc) == 0): return False

    for v in set(pc):
        if (v == m): return True
    return False


reg = '(' + input("Enter the Regular Expression: ") + ')'
str = input("Enter the string w: ")
NFAwithEpsilon(reg)
m= len(reg)
print(evaluate(str))




