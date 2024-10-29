#2 reactions

targetreactants = ["C","C","D"]
targetproducts = ["A"]

endingreactants = targetreactants
endingproducts = targetproducts

reaction1 = [["A"],["B","B"],57.9]
reaction2 = [["C","C","D"],["B","B"],-113.1]

reactions = [
[["A"],["B","B"],57.9],
[["C","C","D"],["B","B"],-113.1]
]

totalenthalpy =0

reactionamount = 2
i=0
for l in range(50):
  j=0
  if i>=len(targetreactants):
    i = 0
  elif i>=len(targetproducts):
    i = 0
  try:
    x=endingreactants+endingproducts
    #print(x)
    x=x[0]
  except:
    break
  reactionsused = [False,False]
  for reaction in range(len(reactions)):
    
    try:
      for j in range(len(reactions[reaction][0])):
        print(reactions[reaction][0][j])
        if reactions[reaction][0][j] == endingreactants[i]:
          k=0
          totalenthalpy += reactions[reaction][2]
          reaction1used = True
          for k in range(len(reactions[reaction][0])):
            try:
              endingreactants.remove(reactions[reaction][0][k])

            except:
              endingproducts.append(reactions[reaction][0][k])
          k=0
          for k in range(len(reactions[reaction][1])):
            try:
              endingproducts.remove(reactions[reaction][1][k])
            except:
              endingreactants.append(reactions[reaction][1][k])
    except:
      pass
    if reactionsused[reaction] == False:
      try:
        for j in range(len(reactions[reaction][1])):
          if reactions[reaction][1][j] == endingreactants[i]:
            k=0
            totalenthalpy -= reactions[reaction][2]
            for k in range(len(reactions[reaction][0])):

              try:
                endingproducts.remove(reactions[reaction][0][k])

              except:
                endingreactants.append(reactions[reaction][0][k])

            k=0
            for k in range(len(reactions[reaction][1])):
              try:
                endingreactants.remove(reactions[reaction][1][k])
              except:
                endingproducts.append(reactions[reaction][1][k])
      except:
        pass
  print()
  print(endingreactants)
  print(endingproducts)
  
  print()
  i+=1

print(endingreactants)
print(endingproducts)
print(totalenthalpy)