#2 reactions

targetreactants = ["N2","N2","O2","O2","O2","O2","O2"]
targetproducts = ["N2O5","N2O5"]

endingreactants = targetreactants
endingproducts = targetproducts

reactions = []

def processreactioninput(reaction):
  reactionlist = reaction.split("=")
  
  reactants = reactionlist[0].split("+")
  print(reactants)
  products = reactionlist[1].split("+")
  print(products)
  output = []
  for i in range(len(reactants)):
    try: 
      coefficient = int(list(reactants[i])[0])
      try:
        coefficient = coefficient*10+int(list(reactants[i])[1])
      except:
        coefficient = int(list(reactants[i])[0])
      reactants[i] = reactants[i].removeprefix(str(coefficient))
    except:
      coefficient = 1
    output.append([])
    for j in range(coefficient):
      output[0].append(reactants[i])
  for i in range(len(products)):
    try: 
      coefficient = int(list(products[i])[0])
      try:
        coefficient = coefficient*10+int(list(products[i])[1])
      except:
        pass
      products[i]=products[i].removeprefix(str(coefficient))
    except:
      coefficient = 1
    output.append([])
    for j in range(coefficient):
      output[1].append(products[i])
  output[2] = reaction.split(":")[1]
  print("output--------------------------")
  print(output)
  return output


for i in range(int(input("How many reactions: "))):
  reactions.append([])
  reactions[i].append(processreactioninput(input("Input reaction " + str(i+1) + ":")))

print(reactions)
exit()
reactionsbackup = [
[["H2","H2","O2"],["H2O","H2O"],20000],
[["N2O5","H2O"],["HNO3","HNO3"],100],
[["N2","O2","O2","O2","H2"],["HNO3","HNO3"],1]
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
  reactionsused = [False,False,False,False,False]
  for reaction in range(len(reactions)):
    print(reaction)
    try:
      for j in range(len(reactions[reaction][0])):
        
        if reactions[reaction][0][j] == endingreactants[i]:
          k=0
          totalenthalpy += reactions[reaction][2]
          reactionsused[reaction] = True
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