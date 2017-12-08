# -*- coding:utf-8 -*-
import json

from pprint import pprint 

def addSolutionInfo(id):
    with open('solutions2.json', 'r') as f:
        solutions = json.load(f)
    if str(id) in solutions.keys():
        print("ID exsited, please try again")
        return 
    algo = input("Enter algorithm: ")
    print("Enter code")
    code = input("Enter code: ")
    s = {"algorithm": algo, "code":code}
    solutions[id] = s
    with open("solution2.json", 'w') as f:
        json.dump(solutions, f)

def addCompe():
    with open('competitions2.json', 'r') as f:
        coms = json.load(f)
    with open('solutions2.json', 'r') as f:
        solutions = json.load(f)
    cid = max([int(i) for i in solutions.keys()]) + 1
    newCom = {}
    for i in ["name", "link", "type", "platform", "pic", "hosts", "ddl"]:
        newCom[i] = input("Enter %d"%(i))
    solution = []
    num = input("How many solutins you find?  ")
    for i in range(num):
        rank = input("Rank: ")
        print("The id of this solutions is %d")
        addSolutionInfo(cid)
        solution.append({"rank":rank, "id":cid})
        cid += 1
        
    newCom["solution"] = solution
    coms.append(newCom)
    with open("solutions2.json", "w") as f:
        json.dump(f, coms)