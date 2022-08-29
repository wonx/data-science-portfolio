# Film recommender system
This is an example of a recommender system, used to provide suggestions for items that better a particular use and predict their preferences. Similar systems can be found in online stores, used to display articles that might be interesting to the user, on social networks to recommend content and similar-minded users, or in restaurant and delivery apps to predict places that match the user's tastes, among many other situations.

In this example, the recommender system is used to suggest movies to a particular user, based on the overall movie ratings and the taste of similar-minded users.

## Structure

### Files

- [Main.ipynb](): starting point. Jupyter notebook encompassing the instructions to read the data, calculate the affinity between users, generate the recommendations, plot the graphs and produce output in csv and png format.

- [filemanager.py](): module that includes the `read_input_file()`,  `store_recommended_film()`, `store_personalized_films()` functions, to read the data source, save the recommendations in a general file, or for a user in particular (in `csv` format), respectively.

- [persona.py](): this module contains the `Persona` class, responsible for the creation of the `persona` objects that store all the user data, like the username, ratings, and the classification table. It also includes methods that return this information in an orderly manner.

- [distancia.py](): composed by the abstract class `Distancia(ABC):`, with the subclasses `DistanciaEuclidiana(Distancia)` and `DistanciaPearson(Distancia)`, which are in charge of calculating the distance between users with the two respective algorithms. Moreover, it contains the `newrange()` methods to addapt the score ranges.

- [filmstats.py](): module that contains a set of functions to extract statistical data related to the movies. For instance, `filmmeans(person)` provides the mean ratings for each film; `mostseen()` shows the most popular movies; `notseen(person)` display those moves that have not been watched by a specific user; and `soulmates(persona)` returns those users with whom the reference user shows closer tastes.

- [makegraphs.py](): this module includes the `input_graphs()`, `intermediate_graphs() `, `output_graphs()`, `recommendations_graph()` and `rating_histogram()` functions aimed to generate a set of plots for the processed data

- [recommendations.py](): includes the class `Recommendation`, and inside, the method `classificationtable()`, which generates the classification table for the `Person` objects, by invoking the distance calculation methods in the `distancia.py` module. In this class constructor, the recommendations for non-watched films are calculated for the specified user.

### Data acquisition and preparation

The recommender system depends on a dataset containing a series of movie ratings for a number of users. The dataset included ([input/import.csv]()) has been randomly generated for demonstration purposes, where ratings are stored as numerical values ranging from 1 to 5. A 0 value indicates that a particular film has not been watched by a user.

### Algorithms


#### User affinity

#### Film statistics

### Plots
