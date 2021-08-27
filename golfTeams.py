import csv
import random
import sys
import math

TRUTHVALUE = 'Y'
MINTEAMSIZE = 3

n = len(sys.argv)
if(n == 1):
  print("Too few arguments (needs 1)")
elif(n > 2):
  print("Too many arguments (needs 1)")
else:
  maxNumTeams = int(sys.argv[1])

  readList = []
  with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for row in csv_reader:
      if line_count != -1:
        readList.append([])
        readList[line_count].append(row[0])
        readList[line_count].append(float(row[1]))
        if(row[2] == TRUTHVALUE):
          readList[line_count].append(True)
        else:
          readList[line_count].append(False)
      line_count += 1
  
  list = sorted(readList, key=lambda x:x[1])
  players = []
  for x in list:
    if(x[2]):
      players.append(x[0])
  
  if((maxNumTeams * MINTEAMSIZE) > len(players)):
    numTeams = len(players) // MINTEAMSIZE
  else:
    numTeams = maxNumTeams
  maxTeamSize = math.ceil(len(players) / numTeams)

  tiers = []
  for i in range(maxTeamSize):
    startIndex = i*numTeams
    endIndex = (i+1)*numTeams
    if(endIndex > len(players)):
      endIndex = len(players)
    tiers.append(players[startIndex:endIndex])
  for x in tiers:
    random.shuffle(x)
  
  teamList = []
  for i in range(numTeams):
    team = []
    for x in tiers:
      if(i < len(x)):
        team.append(x[i])
    teamList.append(team)

  for x in teamList:
    print(str(x) + "\n")