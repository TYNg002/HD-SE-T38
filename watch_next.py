# import spaCy module to detect similarity
import spacy

nlp = spacy.load('en_core_web_md')

# function to return movie with greatest similarity in description to a reference movie description
def recommend(ref_movie_desc):
    # create dictionary to track similarity scores of movies, with movie title as key and similarity score as value
    similarity = {}
    # for each movie, obtain similarity score and add to dictionary
    for movie in movies_dict:
        score = movies_dict[movie].similarity(nlp(ref_movie_desc))
        similarity[movie] = score
    # followed guidance on how to return dictionary key with the greatest value
    # https://datagy.io/python-get-dictionary-key-with-max-value/
    max_score_title = max(similarity, key=similarity.get)
    return max_score_title

# create a list from external file of movie titles and descriptions
with open('movies.txt', "r", encoding="UTF-8") as movies:
    movies_list = movies.readlines()

# create a dictionary with movie titles as keys and movie descriptions as values
movies_dict = {}
for movies in movies_list:
    movies = movies.split(":")
    movies_dict[movies[0]] = nlp(movies[1])

ref_movie = ["Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."]

print(f"{ref_movie[0]} is most similar to: {recommend(ref_movie[1])}")