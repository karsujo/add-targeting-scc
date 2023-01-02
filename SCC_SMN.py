class Node:
    def __init__(self, value, type, attr):
        self.value = value
        self.type = type
        self.attr = attr
        self.d = None
        self.f = None


class Graph:
    def __init__(self): 
        self.adj = {}

    def has_node(self, v):
        try:
            self.adj[v]
            return True
        except KeyError:
            return False

    def add_node(self, v):
        if self.has_node(v):
            return False
        else:
            self.adj[v] = {}
            return True
    
    def add_nodes(self, arr):
        for v in arr:
            self.add_node(v)
        return True

    def has_edge(self, start, end): 
        if self.has_node(start) and self.has_node(end):
            try:
                if self.adj[start][end] is True:
                    return True
                return False
            except KeyError:
                return False
        return False

    def add_edge(self, start, end):
        if self.has_node(start) and self.has_node(end):
            self.adj[start][end] = True
            return True
        return False

    def remove_edge(self, start, end):  
        if self.has_edge(start, end):
            del self.adj[start][end]
            return True
        return False

    def remove_node(self, v):
        if self.has_node(v):
            for vertex in self.adj.keys():
                self.remove_edge(vertex, v)
            del self.adj[v]
            return True
        return False

traversal_time = 0
def dfs_visit(G, s, parent, stack):
    global traversal_time
    traversal_time += 1
    s.d = traversal_time

    for v in G.adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(G, v, parent, stack)

    traversal_time += 1
    s.f = traversal_time
    stack.append(s)


def dfs(G, stack):
    parent = {}
    stack = []

    for vertex in list(G.adj.keys()):
        if vertex not in parent:
            parent[vertex] = None
            dfs_visit(G, vertex, parent, stack)

    return stack

def dfs_pass(adj_list, v, visited, stack):
    for u in adj_list[v]:
        if u not in visited:
            visited[u] = v
            dfs_pass(adj_list, u, visited, stack)
    stack.append(v)

def Algo_KOSRAJU(G):    
    # fetch nodes based on finish time --descending order
    stack = dfs(G, [])
    
    # Reverse all edges of graph
    rev_adj = {}

    for vertex in G.adj.keys():
        rev_adj[vertex] = {}

    for vertex in G.adj.keys():
        for u in G.adj[vertex]:
            rev_adj[u][vertex] = True


    # pop from stack and traverse
    visited = {}
    components = []
    i = 0

    while stack != []:
        v = stack.pop()
        # if v is already visited skip iteration
        if v in visited:
            continue
        # if not visitied, get all reachable nodes and insert into component st
        else:
            components.append([])
            if v not in visited:
                visited[v] = True
                dfs_pass(rev_adj, v, visited, components[i])
            
            components.append([])
            i += 1
    
    return components


def print_stack(stk):
    for i in stk:
        print(i.value, i.f)

def print_adjacency_list(adj):
    for v in adj.keys():
        print(v.value, " -> ", end=" ")
        for u in adj[v]:
            print(u.value, end=" ")
        print()

#=========================================================================================================================================

G = Graph()

p_alison = Node('Alison', 'Person', {"Age":27, "Sex":"F"})
pa_bingisss = Node('BingISSS', 'Page', {"Name": "Binghamton ISSS", "Tags": ["International","Student", "University", "Binghamton University"],"Weight":5} )
p_jordan = Node('Jordan', 'Person', {"Age":29, "Sex":"M"})
pa_bingu = Node('BingU', 'Page', {"Name": "Binghamton University", "Tags": ["University","Binghamton", "SUNY"], "Weight": 7} )
pa_culture = Node('Culture', 'Page', {"Name": "WorldCulture", "Tags": ["Culture","Music", "Art"], "Weight":10} )
pa_eurocul = Node('European Culture', 'Page', {"Name": "European Culture", "Tags": ["German","British","Dutch"], "Weight": 11} )
pa_suny = Node('SUNY', 'Page', {"Name": "SUNY", "Tags": ["SUNY","State University of New York","Binghamton", "Buffalo", "Albany"], "Weight":6} )

p_i_srihari = Node('D Srihari', 'Person (Influencer)', {"Age":27, "Sex":"M"})
p_i_stenger = Node('Harvey Stenger', 'Person (Influencer)', {"Age":27, "Sex":"M"})

p_peter = Node('Peter', 'Person', {"Age":20, "Sex":"M"})
p_andrew = Node('Andrew', 'Person', {"Age":22, "Sex":"M"})
p_katie = Node('Katie', 'Person', {"Age":20, "Sex":"F"})

p_ashley = Node('Ashley', 'Person', {"Age":21, "Sex":"F"})
p_brandon = Node('Brandon', 'Person', {"Age":27, "Sex":"M"})
p_matt = Node('Matt', 'Person', {"Age":29, "Sex":"M"})
p_randy = Node('Randy', 'Person', {"Age":21, "Sex":"M"})

p_tom = Node('Tom', 'Person', {"Age":27, "Sex":"M"})

p_liam = Node('Liam', 'Person', {"Age":24, "Sex":"M"})
p_ivannah = Node('Ivannah', 'Person', {"Age":21, "Sex":"F"})

p_c_jbieb = Node('Justin Beiber', 'Infuencer', {"Name": "Binghamton University", "Tags": ["Music"], "Weight": 9})



G.add_nodes([p_alison,pa_bingisss,p_jordan,pa_bingu,pa_culture, pa_eurocul,pa_suny,p_i_srihari,p_i_stenger, p_peter, p_andrew, p_katie, p_ashley, p_brandon, p_matt, p_randy, p_tom, p_c_jbieb, p_ivannah, p_liam])

G.add_edge(p_alison, pa_bingisss)
G.add_edge(pa_bingisss, p_alison)
G.add_edge(pa_bingisss, p_jordan)
G.add_edge(p_jordan, pa_bingisss)
G.add_edge(pa_bingisss, pa_bingu)
G.add_edge(pa_bingu, p_jordan)
G.add_edge(pa_bingisss, pa_culture)
G.add_edge(p_alison, pa_eurocul)
G.add_edge(pa_culture, pa_eurocul)
G.add_edge(pa_suny, pa_bingu)
G.add_edge(pa_bingu, pa_suny)
G.add_edge(pa_bingu, p_i_stenger)
G.add_edge(p_i_stenger, pa_bingu)
G.add_edge(p_i_srihari, p_i_stenger)
G.add_edge(p_i_stenger, p_i_srihari)
G.add_edge(p_peter, p_i_srihari)
G.add_edge(p_andrew, p_peter)
G.add_edge(p_i_stenger, p_katie)
G.add_edge(p_katie, p_andrew)
G.add_edge(p_andrew, p_randy)
G.add_edge(p_i_stenger, p_randy)
G.add_edge(p_randy, p_c_jbieb)
G.add_edge(p_c_jbieb, p_randy)
G.add_edge(pa_culture, p_c_jbieb)
G.add_edge(p_c_jbieb, p_matt)
G.add_edge(p_matt, p_ashley)
G.add_edge(p_tom, p_ashley)
G.add_edge(p_tom, p_brandon)
G.add_edge(p_andrew, p_tom)
G.add_edge(p_tom, p_andrew)
G.add_edge(p_peter, p_liam)
G.add_edge(p_i_srihari, p_ivannah)
G.add_edge(p_ivannah, p_liam)
G.add_edge(p_liam, p_i_srihari)


scc_output = Algo_KOSRAJU(G)

compNames = []

# Component Labeling  
for j in range(len(scc_output)):
    compName = ""
    maxWeight = -1
    for v in scc_output[j]:
        if(v.attr.get("Weight") != None):
            if(v.attr.get("Weight")>maxWeight):
                maxWeight = v.attr.get("Weight")
                cNm = ""
                for i,e in enumerate(v.attr.get("Tags")):
                    cNm = cNm+"-"+e
                compName = cNm
     
    if(compName == ""):
        compName = "-Default"
    compNames.append(compName+"-")



for j in range(len(scc_output)):
    if scc_output[j] != []:
        print("Component [", compNames[j], "] : ", end="\n")
        print("----------------------------------------------------- \n")
        for v in scc_output[j]:
            print(v.value,"(",v.type  ,")")
        print()