#Question 1
def sup21(nombre):
  if nombre >= 21:
    result= True 
  else:
    result=False
  return result


#Question 2
def pair(liste):
  paire=[]
  for i in range(len(liste)):
    if liste[i] % 2 == 0:
      paire.append(liste[i])
  return paire

#Question 3
def ajout4(liste):
  l=[4]
  ajout4 = liste + l
  return ajout4



  