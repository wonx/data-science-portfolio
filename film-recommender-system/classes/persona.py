class Persona:

    def __init__(self, data, films):
        self.__name = data[0]
        self.__ratings = data[1:]
        self.__dic = dict(zip(films, self.__ratings))

    def __str__(self):
        tmp = self.__name + ": " + str(self.__dic)
        return tmp

    def get_name(self):
        return(self.__name)

    def get_ratings(self):
        return(self.__ratings)

    def get_classificationtable(self, title="all"):
        import pandas as pd
        if not hasattr(self, 'classification_table'):
            print("Classification table not yet generated for this person.")
            return

        if title == "all":
            print("\nTaula de classificació completa per afinitat")
            #print(pd.DataFrame.from_dict(self.classification_table, orient='columns'))
            print(pd.DataFrame(self.classification_table).sort_values(by='Distance', axis=0, ascending=False))
        elif title == "raw":
            print("\nRaw classification table per a", self.get_name(), ":")
            for z in range(len(self.classification_table)):
                print(self.classification_table[z])
        else:
            print("\nTaula de classificació per al film "+title+" per "+self.get_name())
            print(pd.DataFrame(self.classification_table).reindex(columns=['Critic', 'Distance', title, title+"_corrected"]).sort_values(by='Distance', axis=0, ascending=False))

    def get_affinity(self):
        import pandas as pd
        if not hasattr(self, 'classification_table'):
            print("Classification table not yet generated for this person.")
            return

        print("\nTaula d'afinitat per a "+self.get_name())
        print(pd.DataFrame(self.classification_table).reindex(columns=['Critic', 'Distance']).sort_values(by='Distance', axis=0, ascending=False))
