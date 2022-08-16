# functions related to extract film stats

# Returns the mean rating for each film (excluding the user itself).
def filmmeans(person):
    import pandas as pd
    #print("Person:", person)
    #print(person.__dict__)
    filmmeans = pd.DataFrame(person.classification_table).mean(axis=0, skipna=True, numeric_only=True).round(decimals=2).to_dict() # mitjana de puntuacions per film, excloent la puntuació del propi usuari
    #print("film means:", filmmeans)
    return filmmeans

# Returns a dictionary with the number of users what watched each film
def mostseen(people, films): # dict with title as key, and frequency as value
    mostseen = {}
    i=0
    for title in films:
        mostseen[title]=0
        for j in range(0,len(people)):
            if people[j]._Persona__dic[title] != 0:
                mostseen[title]+=1
        i+=1
    return mostseen

# Returns a list of not seen films (films with rating 0)
def notseen(person, films): # films not seen by person (object)
    #print(person.get_name(), "no ha vist:")
    i = 0
    notseen = []
    for rating in person.get_ratings():
        #print(films[i], rating)
        if rating == 0: # if not rated
            notseen.append(films[i])
        i+=1
    return notseen # Returns list of film titles not seen by person

# Returns dictionary of soulmates with name as key and distance as value
def soulmates(person):
    soulmates = {}
    #print("Classification table:", person.classificationTable)
    #print("Respecte", person.get_name())
    for line in person.classificationTable:
        #print("Critic:", line['Critic'], "\tAfinitat:", line['Distance'])
        if line['Distance'] >= 0.75:
            soulmates[line['Critic']] = round(line['Distance'], 2)
    return soulmates
