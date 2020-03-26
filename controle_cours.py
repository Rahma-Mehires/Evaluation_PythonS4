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
def ajout4(liste1):
  l=[4]
  ajout4 = liste1 + l
  return ajout4

#Question 4
def to_strings(dictionnaire):
  l1=[]
  for clé, val in dictionnaire.items():
    l1.append(str(clé) + ":" + str(val))
  return l1

#Question  5
def extremites(liste2):
  l2= liste2[:2]  + liste2[-2:]
  return l2

#Question 6
class Mot():
  def __init__ (self,mot):
    self.mot = mot
  def comptelettre(self,cara):
    if cara.lower() in self.mot.lower():
      print(self.mot.count(cara.lower()))
 
#Question 7       
def tri_et_inverse(liste3):
    l3=[]
    for x in reversed(liste3):
        l3.append(x)
    return (sorted(liste3), l3)
       

#Question 8 
#class fake_input:
#  def __init__(self, saisies):
#    self._iter = iter(saisies)
#  def __call__(self, *args, **kwargs):
#    return next(self._iter)   
#def aller_a_paris(input_call=input):
#  saisie = input
#  nb=0
#  while saisie != "Paris":
#    nb=nb+1
#  return [nb,saisie]

#Question 9
ville_nom_pays = {"Paris":"France","Berlin":"Allemagne","Madrid":"Espagne","Moscou":"Russie"} 

#Question 10
class Pays():
  def __init__ (self, nom, visa):
    self.nom = nom
    self.visa = visa


ville_pays = {"Paris" : Pays("France", False),"Berlin" : Pays("Allemagne", False),"Madrid" : Pays("Espagne", False),"Moscou" : Pays("Russie", True)}

    
if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
 
