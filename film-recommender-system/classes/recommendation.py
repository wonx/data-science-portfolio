class Recommendation:
    def __init__(self, person, people, films, minrating=1.5): # person (object instance of Persona), people (list of all Persona objects), films (tuple with all film titles)
        print("\nRecommendation module:")
        from filmstats import mostseen, notseen, filmmeans
        self.__recommendation = {}
        self.__meanratings = {}

        # Controlar que la classificaation table existeixi
        print(" ", person.get_name(), "has not seen", notseen(person, films))
        for title in films:
            self.__popularity = mostseen(people, films)[title]/len(people) # votes by the amount of people
            if title in notseen(person, films):
                print(" ", title, "Popularity: ", round(self.__popularity*100, 1), "%")
                #print("Anem a veure si es recomana...")
                self.__meanratings = filmmeans(person)
                #print("Mean ratings:", self.__meanratings)
                print(" ", title, "Corrected:", self.__meanratings[title+"_corrected"], "; Corrected by popularity:", round(self.__meanratings[title+"_corrected"]*self.__popularity, 2))
                if self.__meanratings[title+"_corrected"]*self.__popularity >= minrating: # at least a rating of "minrating" after correction
                    self.__recommendation[title] = round(self.__meanratings[title+"_corrected"]*self.__popularity, 2)
                    #print("Sí!")

    def __str__(self):
        tmp = "The recommended films are: ", self.get_recommendation()
        return tmp

    def get_recommendation(self):
        return self.__recommendation

    # Generates the rating classification table for each user (including corrected ratings)
    def classificationtable(person, people, films, distancetype="pearson"):
        import distancia as d
        print("\nGenerating the classification table for", person.get_name(), "...")
        person.classification_table = []

        for j in range(0,len(people)):
            classification = {} # local variable, for temporally storing each item for the classification table
            if people[j].get_name() != person.get_name():
                #print("\nComparem",  person.get_name(), "amb", people[j].get_name())
                if distancetype == "euclidean":
                    dist = d.DistanciaEuclidiana.Dist(person.get_ratings(), people[j].get_ratings())
                    dist=1-dist # Per a que nombres més alts indiquin similitud
                elif distancetype == "pearson":
                    dist = d.DistanciaPearson.Dist(person.get_ratings(), people[j].get_ratings())
                else:
                    print("Distance type must be either 'euclidean' or 'pearson'")
                    return

                classification['Critic'] = people[j].get_name() # Afegim clau 'critic' al diccionari
                classification['Affinity'] = round(dist,2)

                for z in films: # Per cada peli..
                    correccio=round(people[j]._Persona__dic[z]*dist, 2)
                    classification[z] = people[j]._Persona__dic[z]
                    classification[z+'_corrected'] = correccio
                    
                person.classification_table.append(classification)

        print("...done.")
        return person.classification_table # list of dictionaries with mean film ratings