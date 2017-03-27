import json

global heData
heData = {}
global dbData
dbData = {}
global mean
global teams
teams = []
dumpClass = {'teamId':"", 'members':[], 'meanScore':0}


def readData():
    global heData
    global dbData
    with open('he.json') as data:
        readData = json.load(data)
        heData = readData
    with open('db.json') as data:
        readData = json.load(data)
        dbData = readData

def findMean():
    tot = 0
    for data in heData:
        temp = float(data['score'])
        tot += temp
    mean = tot/len(heData)

def parsedb():
    global ids
    global teams
    teams = []
    for entry in dbData:
        team = {'teamId':"", 'members':[]}
        team['teamId'] = entry['teamId']
        users = entry['users']
        team['members'] = users
        teams.append(team)

def dumpFromTeams():
    writeFile = open('newjson.json','w')
    writeFile.write('[')
    toDump = False
    for team in teams:
        dumpClass = {'teamId':"", 'members':[], 'meanScore':0}
        members = team['members']
        dumpClass['teamId'] = team['teamId']
        dumpClass['meanScore'] = 0
        n = 0
        tot = 0
        for member in members:
            id = member['hackerEarthId']
            for entry in heData:
                #print("+",entry['email'])
                #print('-',id)
                temp = entry['email']
                if(str(id) == str(temp)):
                    dumpClass['members'].append(id)
                    tot += float(entry['score'])
                    n += 1
                    toDump = True
        if(n!=0):
            dumpClass['meanScore'] = tot/n
        if(n!=0):
            print(n)
            trump = json.dumps(dumpClass)
            writeFile.write(str(trump)+',\n')
    writeFile.write(']')
readData()
findMean()
parsedb()
dumpFromTeams()
