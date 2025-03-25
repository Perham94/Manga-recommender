import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("manga.csv")
df = df.dropna(subset=['Title', 'Genres'])

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Genres'])

def recommend_manga(title):
    if title not in df['Title'].values:
        return ["Manga not found."]
    
    idx = df[df['Title'] == title].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-6:-1][::-1]  # Top 5
    
    recommendations = df['Title'].iloc[similar_indices].tolist()
    return recommendations
