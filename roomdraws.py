import numpy as np
import numpy.random as random
## param

maxPerTeam = np.float64(4)

names = {0:{0:{0:'Richard', 1:'Saman'}, 1:{0:'Jonna', 1:'Magnus'}, 2:{0:'Erik', 1:'NJ', 2:'Hannes'}},
         1:{0:{0:'Karin', 1:'SomeoneElse'} }
         }

numberOfPeople = 0

# we so dirty, inefficient counting
for floor in names.iterkeys():
    for room in names[floor].iterkeys():
        for people in names[floor][room]:
            numberOfPeople += 1

minTeams = int(np.ceil(numberOfPeople/maxPerTeam))

teams = {}
availableTeams = np.arange(0, minTeams)
for i in availableTeams:
    teams[i] = []



for floor in names.iterkeys():
    for room in names[floor].iterkeys():
        nPeople = len(names[floor][room])
        rooms = random.choice(availableTeams, replace=False, size=nPeople)
        for econSlave in names[floor][room]:
            teams[rooms[econSlave]].append(names[floor][room][econSlave])

print teams