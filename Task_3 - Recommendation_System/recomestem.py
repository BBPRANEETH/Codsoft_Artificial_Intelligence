import pandas as pd
data = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    
    'title': ['Toy Story', 'Jumanji', 'Batman Begins', 'Spider-Man', 'Titanic', 'The Godfather', 'Interstellar', 'Jurassic Park', 'The Fall Guy', 'Focus'],
    
    'genres': ['Animation|Children|Comedy', 'Adventure|Children|Fantasy', 'Action|Crime|Drama',
               'Action|Adventure|Sci-Fi', 'Action|Drama|Romance', 'Action|Gangster|Mafia','Mystery|Sci-fi|Adventure', 'Action|Adventure|Fantasy','Action|Comedy|Thriller', 'Action|Romance|Crime']
}

movies_df = pd.DataFrame(data)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)

tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres'])

feature_names = tfidf_vectorizer.get_feature_names_out()
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(movie_title, tfidf_matrix, movies_df, top_n=5):
    # Find the index of the movie
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    
    # Calculate cosine similarity between the selected movie and all movies
    cosine_similarities = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    similar_indices = cosine_similarities.argsort()[:-top_n-1:-1]
    
    recommendations = [(movies_df['title'][i], cosine_similarities[i]) for i in similar_indices if i != idx]
    
    return recommendations[:top_n]
  #set the movie title
movie_title = 'Focus'
recommendations = get_recommendations(movie_title, tfidf_matrix, movies_df, top_n=3)

#print recommendations as per movie
print(f"Top recommendations for '{movie_title}':")
for recommendation in recommendations:
    print(recommendation)
