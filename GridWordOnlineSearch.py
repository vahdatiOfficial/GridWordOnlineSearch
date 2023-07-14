class Problem:
    def __init__(self,gridWord) -> None:
        self.gridWord = gridWord
    def IsGoal(self,s):
        if(self.gridWord[s] == 'G'):
            return True
        else:
            return False
def newAgent(agent,action):
    index =  agent
    if(action == "U"):
        return (index - n)
    if(action == "D"):
        return (index + n)
    if(action == "R"):
        return (index + 1)
    if(action == "L"):
        return (index - 1)
def problemActions(problem,agent):
    index = agent
    lis = []
    if((index - n) > -1):
        if(problem.gridWord[index - n] != '#'):
            lis.append("U")
    if((index + 1) % n != 0):
        if(problem.gridWord[index + 1] != '#'):
            lis.append("R")
    if((index + n) < (n*m)):
        if(problem.gridWord[index + n] != '#'):
            lis.append("D")
    if(index % n != 0):
        if(problem.gridWord[index - 1] != '#'):
            lis.append("L")
    return lis
def Pop(list):
    temp = list[0]
    list.remove(temp)
    return temp
def IsEmpty(list):
    return len(list) == 0

def printS(list):
    s = ""
    for solu in list:
        s += solu + " "
    s = s[:-1]
    return s
def OnlineSearchDfs(Problem,primS):
    untried = dict()
    unbacktracked = dict()
    result = dict()
    solution = []
    msg = ""
    s = None
    action = None
    while True:
        if (problem.IsGoal(primS)):
            msg = "Goal reached"
            break
        if(primS not in untried.keys()):
            untried[primS] = problemActions(problem,primS)
        if(s is not None):
            result[(s,action)] = primS
            if(primS not in unbacktracked.keys()):
                unbacktracked[primS] = []
            unbacktracked[primS].append(s)
        if(IsEmpty(untried[primS])):
            if(IsEmpty(unbacktracked[primS])):
                msg = "stopped"
                break
            else:
                flag = False
                unbacktrackedPop = unbacktracked[primS].pop()
                for (st,b) in result.keys():
                    if(result[(st,b)] == unbacktrackedPop):
                        flag = True
                        action = b
                        primS = newAgent(primS,action)
                        s = None
                        solution.append(action)
                        break
                if flag:
                    continue;
        else:
            action = Pop(untried[primS])
            solution.append(action)
        s = primS
        primS = newAgent(s,action)
    return msg , solution
global m , n
m , n = input().split(" ")
m = int(m)
n = int(n)
gridWord = []
for i in range(0,m):
    for j in input():
        gridWord.append(j)
problem = Problem(gridWord)
agent = problem.gridWord.index("A")
a = OnlineSearchDfs(problem,agent)
print(printS(a[1]))
print(a[0])
