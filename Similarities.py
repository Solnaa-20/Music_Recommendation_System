import numpy as np

def euclidean_distance(user1_ratings, user2_ratings):
    common_ratings = (user1_ratings > 0) & (user2_ratings > 0)
    if common_ratings.sum() == 0:
        return np.inf
    user1_common = user1_ratings[common_ratings]
    user2_common = user2_ratings[common_ratings]

    distance = np.sqrt(np.sum((user1_common - user2_common) ** 2))

    return distance

def calculate_all_distances(target_user,ratings_df):
    distances = {}
    target_ratings = ratings_df.loc[target_user]

    for other_user in ratings_df.index:
        if other_user == target_user:
            continue

        other_ratings = ratings_df.loc[other_user]

        distance = euclidean_distance(
            target_ratings,
            other_ratings
        )
        distances[other_user] = distance
    return distances

def find_similar_users(target_user,ratings_df):
    distances = calculate_all_distances(
        target_user,
        ratings_df
    )
    sorted_users = sorted(
        distances.items(),\
        key = lambda x:x[1]
    )

    return sorted_users

def get_top_neighbors(target_user, ratings_df, k = 5):
    similar_users = find_similar_users(
        target_user,
        ratings_df
    )
    return similar_users[:k]

def display_similar_users(target_user,ratings_df,k=5):
    neighbors = get_top_neighbors(
        target_user,
        ratings_df,
        k
    )
    print(f"\nUsers most similar to {target_user}:\n")

    for i,(user,distance) in enumerate(neighbors,start=1):
        print(f"{i}.{user}- Distance: {distance:2f}")
