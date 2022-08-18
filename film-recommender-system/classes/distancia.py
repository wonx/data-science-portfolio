from abc import ABC, abstractmethod

class Distancia(ABC): # Ha de ser una classe abstracta

    def __init__(self, persona1, persona2, algorithm="pearson"):
       pass
   
    def __str__(self):
        tmp = "The distance is: "+str(self.get_distance())
        return tmp

    def get_distance(self):
         return self.__distance

    # Defining abstract method .Dist()
    @abstractmethod
    def Dist(x,y):
        pass

    # converts a range value to a new one (e.g. -1:1 to 0:1)
    def newrange(OldValue, OldMin, OldMax, NewMin=0, NewMax=1):
        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + 0
        return NewValue

class DistanciaEuclidiana(Distancia):
    def __init__(self,p,q):
        print('DistanciaEuclidiana class constructor')

    # Rep dos arrays unidimensionals amb puntuacions, i calcula la distancia
    # euclidiana entre cadascun dels elements.
    # Els elements amb valor 0 són els no puntuats, i no es tenen en compte.
    def Dist(p,q):
        import numpy as np
        distance = []
        #print(p)
        #print(q)

        distance = [np.sqrt(np.sum((p[i]-q[i])**2)) if p[i] != 0 else np.nan for i in range(len(p))] 

        distance=np.nanmean(distance)
        #print("\nDistancia:", distance)
        distance=Distancia.newrange(distance, 1, 5)
        return np.round(distance, 3)


class DistanciaPearson(Distancia): # Utilitzar Numpy
    def __init__(self):
        print('Class constructor ', self.__name__)

    def Dist(x,y):
        import numpy as np
        import numpy.ma as ma # masked array, per a gestionar els valors Nan
        distance = 0

        x = [np.nan if i == 0 else i for i in x] # replace 0 to Nan
        y = [np.nan if i == 0 else i for i in y]

        # The distance is just one value of the correlation matrix
        distance=ma.corrcoef(ma.masked_invalid(x),ma.masked_invalid(y))[0, 1]
        
        # If sample size is not big enough (n<3), the correlation will result in 1,
        # which is wrong, so we set it back to 0.
        if distance == ma.corrcoef(ma.masked_invalid(x),ma.masked_invalid(y))[0, 0]:
            distance = 0

        # Replace masked values with np.nan
        if ma.is_masked(distance): distance = np.nan

        # Convert the distance range from -1:1 to 0:1
        distance=Distancia.newrange(distance, -1, 1)

        #print("\nDistancia:", distance)
        return np.round(distance,3)
