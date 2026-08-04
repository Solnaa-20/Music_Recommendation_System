
#Start
import numpy as np
def euclidean_distance(user1_ratings, user2_ratings):
    common_ratings = (user1_ratings > 0) & (user2_ratings > 0)
    if common_ratings.sum() == 0:
        return np.inf
    user1_common = user1_ratings[common_ratings]
    user2_common = user2_ratings[common_ratings]

    distance = np.sqrt(np.sum((user1_common - user2_common) ** 2))

    return distance
