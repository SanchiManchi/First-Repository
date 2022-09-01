count = 0
NameList = []
AssistList = []
ShotList = []
GoalList = []
SuccInd = 0
SuccIndList = []
highestSI = 0 
win = 0

while count < 3:
  Name = input("Player Name:")
  NameList.append(Name)
  Assists = int(input("No. of assists:"))
  if Assists > 50:
    Assists = 50
    AssistList.append(Assists)
  else:
    AssistList.append(Assists)
  Shots = int(input("No. of Shots:"))
  if Shots > 100:
    Shots = 100
    ShotList.append(Shots)
  else:
    ShotList.append(Shots)
  Goals = int(input("No. of goals:"))
  if Goals > 40:
    Goals = 40
    GoalList.append(Goals)
  else: 
    GoalList.append(Goals)
  SuccInd = (1*Assists) + (2*Shots) + (3*Goals)
  SuccIndList.append(SuccInd)
  print("Name:", Name, "Success Index:", SuccInd)
  if highestSI < SuccInd:
    win = count
    highestSI = SuccInd
  count = count + 1

Num = 0
TotSuccInd = 0

while Num < 3:
  TotSuccInd = TotSuccInd + SuccIndList[Num]
  Num = Num + 1

Avg = 0
Avg = TotSuccInd/3

print("Average Squad Success Index:", Avg)

print("Highest Success Index:", SuccIndList[win], "by:", NameList[win],"Their Goals:", GoalList[win], "Their Assists:", AssistList[win], "Their Shots:", ShotList[win]) 
