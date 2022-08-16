import pandas as pd
import os

# path = "/content/drive/My Drive/Colab Notebooks/Projecte 1/"
path = "./" # When working locally


def read_input_file():
  try:
    df = pd.read_csv(path+'input/import.csv')
  except IOError:
    print("Error al obrir el fitxer!")
    return
  return df

def store_recommended_film(target, recommendation):

  fullpath=path+"output/"
  # Global recommendation file
  g = open(fullpath+"Recomanacions.txt", "a")

  # Creem una string amb els films recomanats, ordenats per puntuació, i separats per comes.
  filmlist=""
  filmlist+=', '.join('{0} ({1})'.format(key,val) for key,val in sorted(recommendation.items(), key=lambda x:x[1], reverse=True))
  g.write("Films recomanats per a "+target+": "+filmlist+".\n")
  g.close()
  print("Fitxer "+fullpath+"Recomanacions.txt actualitzat amb les recomanacions per a "+target)

def store_personalized_films(target, recommendation):
  # Personalized recommendation file (in csv format)
  fullpath=path+"output/detailed recommendations/"
  os.makedirs(os.path.dirname(fullpath), exist_ok=True) # If the folder does not exist, we create it
  f = open(fullpath+target+"_recommendations.csv", "wt")
  f.write("Title,Adjusted rating\n")
  for film in sorted(recommendation.items(), key=lambda x:x[1], reverse=True):
    f.write(film[0]+","+str(film[1])+"\n")
  f.close()
  print("Creat fitxer "+fullpath+target+"_recommendations.csv")
