import csv
import random

TRUTHVALUE = 'Y'

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
    players.append(x)
l = len(players) // 4
tierList = [[],[],[],[],[]]
for i in range(l):
  tierList[0].append(players[i])
  tierList[1].append(players[i+l])
  tierList[2].append(players[i+2*l])
  tierList[3].append(players[i+3*l])
  if(i+4*l < len(players)):
    tierList[4].append(players[i+4*l])
# for x in tierList:
#   for y in x:
#     print(y[0])
#   print()
for x in tierList:
  random.shuffle(x)
teamList = []
for i in range(l):
  teamList.append([])
  teamList[i].append(tierList[0][i][0])
  teamList[i].append(tierList[1][l-i-1][0])
  teamList[i].append(tierList[2][i][0])
  teamList[i].append(tierList[3][l-i-1][0])
  if(i < len(tierList[4])):
    teamList[i].append(tierList[4][i][0])
for x in teamList:
  print(str(x) + "\n")