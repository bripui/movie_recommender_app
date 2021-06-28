"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""


from utils import movies


def recommend_random(liked_items, k=5):
    """
    return k random unseen movies for user 
    """
    # dummy implementation
    return movies.sample(k)



def recommend_most_popular(liked_items, movie_item_avg, k=5):
    """
    return k most popular unseen movies for user
    """
    return None




if __name__ == '__main__':
    print(recommend_random([1, 2, 3]))




