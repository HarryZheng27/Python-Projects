#2 reactions

targetreactants = ["C","C","D"]
targetproducts = ["A"]

endingreactants = targetreactants
endingproducts = targetproducts

reaction1 = [["A"],["B","B"],57.9]
reaction2 = [["C","C","D"],["B","B"],-113.1]

reactions = [[["A"],["B","B"],57.9],[["C","C","D"],["B","B"],-113.1]]

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
  reaction1used = False
  reaction2used = False
  try:
    for j in range(len(reaction1[0])):

      if reaction1[0][j] == endingreactants[i]:
        k=0
        totalenthalpy += reaction1[2]
        reaction1used = True
        for k in range(len(reaction1[0])):
          try:
            endingreactants.remove(reaction1[0][k])

          except:
            endingproducts.append(reaction1[0][k])
        k=0
        for k in range(len(reaction1[1])):
          try:
            endingproducts.remove(reaction1[1][k])
          except:
            endingreactants.append(reaction1[1][k])
  except:
    pass
  print()
  print(endingreactants)
  print(endingproducts)
  print()
  j=0
  try:
    for j in range(len(reaction2[0])):
      if reaction2[0][j] == endingreactants[i]:
        totalenthalpy += reaction2[2]
        reaction2used = True
        k=0
        for k in range(len(reaction2[0])):
          try:
            endingreactants.remove(reaction2[0][k])
          except:
            endingproducts.append(reaction2[0][k])
        k=0
        for k in range(len(reaction2[1])):
          try:
            endingproducts.remove(reaction2[1][k])
          except:
            endingreactants.append(reaction2[1][k])
  except:
    pass
  print()
  print(endingreactants)
  print(endingproducts)
  print()
  if reaction1used == False:
    try:
      for j in range(len(reaction1[1])):
        # print(endingreactants[i])
        # print()
        # print(reaction1[1][j])
        # print("------")
        if reaction1[1][j] == endingreactants[i]:
          k=0
          totalenthalpy -= reaction1[2]
          for k in range(len(reaction1[0])):

            try:
              endingproducts.remove(reaction1[0][k])

            except:
              endingreactants.append(reaction1[0][k])

          k=0
          for k in range(len(reaction1[1])):
            try:
              endingreactants.remove(reaction1[1][k])
            except:
              endingproducts.append(reaction1[1][k])
    except:
      pass
  print()
  print(endingreactants)
  print(endingproducts)
  print()
  if reaction2used == False:
    try:
      for j in range(len(reaction2[1])):
        if reaction2[1][j] == endingreactants[i]:
          totalenthalpy -= reaction2[2]
          k=0
          for k in range(len(reaction2[0])):
            try:
              endingproducts.remove(reaction2[0][k])
            except:
              endingreactants.append(reaction2[0][k])
          k=0
          for k in range(len(reaction2[1])):
            try:
              endingreactants.remove(reaction2[1][k])
            except:
              endingproducts.append(reaction2[1][k])
    except:
      pass
  print()
  print(endingreactants)
  print(endingproducts)
  print("-----------------------------------------------------------------")
  i+=1

print(endingreactants)
print(endingproducts)
print(totalenthalpy)
