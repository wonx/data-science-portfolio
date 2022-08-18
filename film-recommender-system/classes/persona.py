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
            print("\nWhole classification table by user affinity")
            #print(pd.DataFrame.from_dict(self.classification_table, orient='columns'))
            display(pd.DataFrame(self.classification_table).sort_values(by='Affinity', axis=0, ascending=False))
        elif title == "raw":
            print("\nRaw classification table for", self.get_name(), ":")
            for z in range(len(self.classification_table)):
                print(self.classification_table[z])
        else:
            print("\nClassification table of "+title+" for "+self.get_name())
            display(pd.DataFrame(self.classification_table).reindex(columns=['Critic', 'Affinity', title, title+"_corrected"]).sort_values(by='Affinity', axis=0, ascending=False))

    def get_affinity(self):
        import pandas as pd
        if not hasattr(self, 'classification_table'):
            print("Classification table not yet generated for this person.")
            return

        print("\nAffinity table for "+self.get_name())
        display(pd.DataFrame(self.classification_table).reindex(columns=['Critic', 'Affinity']).sort_values(by='Affinity', axis=0, ascending=False))
