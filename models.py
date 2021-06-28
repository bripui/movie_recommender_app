from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import pairwise
from scipy.sparse import csr_matrix
import sklearn

import pickle
from fuzzywuzzy import process

from utils import movies, ratings_long, ratings

# create model  
user_item = csr_matrix((ratings_long['rating'], (ratings_long['userId'], ratings_long['movieId'])))
# initialize the unsupervised model
model = NearestNeighbors(metric='cosine')
# fit it to the user-item matrix
model.fit(user_item)

pickle.dump(model, open('./models/NN_cosine.sav', 'wb'))