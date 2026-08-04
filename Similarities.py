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