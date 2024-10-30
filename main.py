import random

reactions = []

def processreactioninput(reaction):
  try:
    reactionlist = str(reaction.split(":")[0]).split("=")
  except:
    reactionlist = reaction.split("=")
  
  reactants = reactionlist[0].split("+")
  #print(reactants)
  products = reactionlist[1].split("+")
  #print(products)
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
  try:
    output[2] = float(reaction.split(":")[1])
  except:
    pass
  try:
    output.remove(output[3])
  except:
    pass
  #print("output--------------------------")
  #print(output)
  return output


for i in range(int(input("How many reactions: "))):
  reactions.append(processreactioninput(input("Input reaction " + str(i+1) + ": ")))

print(reactions)
targetreaction = processreactioninput(input("Target Reaction: "))
targetreactants = targetreaction[0]
targetproducts = targetreaction[1]
finalreactants = targetreaction[0]
finalproducts = targetreaction[1]
print(targetreaction)
endingreactants = targetreactants
endingproducts = targetproducts


totalenthalpy =0

reactionamount = 2
i=0
for multiple in range(10):
  for l in range(100):
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
    reaction = random.randint(0,len(reactions)-1)
      #print(reaction)
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
  finalreactants.append(targetreactants)
  finalproducts.append(targetproducts)
  endingreactants=finalreactants
  endingproducts=finalproducts

print(endingreactants)
print(endingproducts)
print("enthalpy change---------------------------------------")
print(totalenthalpy/multiple)