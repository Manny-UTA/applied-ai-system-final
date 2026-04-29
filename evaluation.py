from src.recommender import recommend_songs, load_songs

def evaluate_system():
    songs = load_songs("data/songs.csv")

    test_users = [
        {"genre": "pop", "mood": "happy", "energy": 0.7},
        {"genre": "lofi", "mood": "calm", "energy": 0.2},
        {"genre": "edm", "mood": "excited", "energy": 0.9},
    ]

    print("\n--- Evaluation Results ---")

    for i, user in enumerate(test_users):
        recs = recommend_songs(user, songs, k=3)
        print(f"Test {i+1}: Returned {len(recs)} songs")

        if len(recs) == 3:
            print("PASS")
        else:
            print("FAIL")


if __name__ == "__main__":
    evaluate_system()