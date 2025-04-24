import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from tqdm import tqdm

def recommend_songs(target_song_name, data, numerical_columns):
    target_song = data[data['name'].str.lower() == target_song_name.lower()].head(1)

    if target_song.empty:
        print("Song not found. Check the name and try again.")
        return None
    
    print(f"\nFinding songs similar to: {target_song_name}\n")
    
    target_features = target_song[numerical_columns].values[0]

    candidates = data[data['name'].str.lower() != target_song_name.lower()].copy()
    distances = []

    print("Calculating similarity...")
    for _, row in tqdm(candidates.iterrows(), total=candidates.shape[0]):
        other_features = row[numerical_columns].values
        dist = np.sum(np.abs(target_features - other_features))
        distances.append(dist)

    candidates['distance'] = distances

    recommendations = candidates.sort_values('distance')[['artists', 'name', 'distance']].head(5)
    print("\nTop 5 Recommended Songs:")
    print(recommendations.to_string(index=False))

def load_and_prepare_data():
    data = pd.read_csv(r"D:\\TANYA\\INTERNSHIPS\\CODSOFT\\PROJECTS\\CODSOFT\\spotify.csv")
    data_cleaned = data.drop(columns=['id', 'name', 'artists', 'release_date', 'year'])
    numerical_columns = data_cleaned.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).columns
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data_cleaned[numerical_columns]), columns=numerical_columns)

    kmeans = KMeans(n_clusters=10, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(normalized_data)
    data['cluster'] = clusters
    
    return data, numerical_columns

def play_song_recommendation_game():
    print("Welcome to Groove!🎶")
    data, numerical_columns = load_and_prepare_data()

    while True:
        target_song_name = input("Enter the name of the song you want recommendations for: ").strip()
        recommend_songs(target_song_name, data, numerical_columns)
        
        again = input("Do you want more song recommendations? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for using Groove!🎶")
            break

if __name__ == "__main__":
    play_song_recommendation_game()