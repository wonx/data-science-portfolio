# -*- coding: utf-8 -*-

"""Import libraries and classes"""

import matplotlib.pyplot as plt
import matplotlib

# path = "/content/drive/My Drive/Colab Notebooks/Projecte 1/"
path = "./"

def recommendations_graph(d): # expects a dictionary
	import pandas as pd
	df = pd.DataFrame(d, index=[0])
	df = df.transpose()
	df = df.sort_values(0, ascending=True)
	print(repr(df))
	plt.rcParams['figure.figsize'] = [4, 4]
	df.plot(kind='barh', edgecolor = "black", linewidth=1)
	plt.legend().set_visible(False)
	plt.title("Corrected scores for recommendations")
	plt.ylabel("Film")
	plt.xlabel("Corrected score")
	plt.show()
	
def rating_histogram(d, classification_table):
	import pandas as pd
	print(d)
	for title in d.keys():
		ratings=pd.DataFrame(classification_table).reindex(columns=[title]).sort_values(by=title, axis=0, ascending=False)
		ratings = ratings.groupby(title).size()
		ratings = ratings.drop(0) # delete rating 0
		i = 1
		for index, row in ratings.iteritems():
			if index != i: ratings.loc[i] = 0
			i +=1
		ratings = ratings.sort_index(ascending=True)
		print(ratings)
		plt.rcParams['figure.figsize'] = [4, 4]
		ratings.plot(kind='bar', width=1, edgecolor = "black", linewidth=1)
		plt.title("Voting histogram for "+title)
		plt.ylabel("Frequency")
		plt.xlabel("Score")
		plt.xticks(range(0,6))
		plt.show()


def input_graphs(df):
    
	"""Plot graphs based on input"""

	##mean of each film
	plt.figure()
	matplotlib.style.use('ggplot')
	plt.title("Mean rating for each film")
	plt.ylabel("Rating")
	df.mean().sort_values(ascending=False).plot(kind='bar')
	plt.savefig(path+"output/raw data/Mean ratings.png")

	##detailed rating of each film
	i = 0
	plt.rcParams['figure.figsize'] = (6,2)
	for column in df.columns[1:]:
		plt.figure()
		plt.xticks([])
    #plt.xticks(df.index, df["Persona"].values, rotation=90)
		plt.title("Ratings for film "+column)
		plt.ylabel("Rating")
		df[column].plot()
		plt.axhline(y=df[column].mean(), color='b', linestyle='-')
		i += 1
		plt.savefig(path+"output/raw data/"+"Film"+str(i)+"-"+column+'.png')

	##popularity of each film
	x = []
	y = []
	for column in df.columns[1:]:
		seriesObj = df.apply(lambda x: True if x[column] > 0 else False, axis=1)
		numOfRows = len(seriesObj[seriesObj == True].index)
		x.append(column)
		y.append(numOfRows)
	y, x = zip(*sorted(zip(y, x), reverse=True))
	c = range(len(y))
	plt.rcParams['figure.figsize'] = (10,4)
	#matplotlib.style.use('ggplot')
	fig = plt.figure()
	plt.title("Amount of people that has watched each film")
	plt.ylabel("# people")
	ax1 = fig.add_subplot(111)
	ax1.bar(c, y)
	plt.xticks(c, x, rotation=90)
	plt.savefig(path+"output/raw data/Popularity.png")


def intermediate_graphs(target, classification_table):
  x = []
  y = []
  for i in range(0,len(classification_table)):
    x.append(classification_table[i]['Critic'])
    y.append(classification_table[i]['Distance'])
  plt.rcParams['figure.figsize'] = (20,5)
  y, x = zip(*sorted(zip(y, x), reverse=True))
  c = range(len(y))
  fig = plt.figure()
  plt.title("Affinity between "+target+" and the rest of users")
  plt.ylabel("Distance")
  ax2 = fig.add_subplot(111)
  ax2.bar(c, y)
  plt.xticks(c, x, rotation=90)
  plt.savefig(path+"output/distances/Distàncies"+target+'.png')


def output_graphs(df, recommendation):
  plt.rcParams['figure.figsize'] = (6, 6)
  labels = 'No vista', '1', '2', '3', '4', '5'
  df[recommendation].value_counts().plot.pie(subplots=True, labels=labels, autopct='%1.1f%%')
  plt.title("Distribució de les puntuacions per al film "+recommendation)
  plt.savefig(path+"output/detailed recommendations/"+"La recomanació és... "+recommendation+'!.png')
  
def affinity_heatmap(people, films, distancealgorithm):
	import pandas as pd
	import recommendation as r

	affinity = pd.DataFrame()
	# This one is just to obtain the dataframe headers
	people[0].classification_table = r.Recommendation.classificationtable(people[0], people, films, distancealgorithm)
	headers = pd.DataFrame(people[0].classification_table).reindex(columns=['Critic'])
	affinity = headers

	print(affinity)
	for k in range(0,len(people)):
	    # We generate the classification table for all users.
	    people[k].classification_table = r.Recommendation.classificationtable(people[k], people, films, distancealgorithm)
	    a = pd.DataFrame(people[k].classification_table).reindex(columns=['Critic', 'Distance'])
	    a = a.rename(columns={"Distance": people[k].get_name()})
	    affinity = pd.merge(affinity, a, how="outer")
	plt.rcParams['figure.figsize'] = (10, 10)
	plt.matshow(affinity.corr())
	print(range(affinity.shape[1]))
	print(affinity.columns[1:])
	plt.xticks(range(affinity.shape[1]-1), affinity.columns[1:], fontsize=8, rotation=90)
	plt.yticks(range(affinity.shape[1]-1), affinity.columns[1:], fontsize=8, rotation=0)
	plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    print("Testing this as a script")
    """
    input_graphs(df)
    intermediate_graphs()
    output_graphs(df,'Pulp Fiction')
    """