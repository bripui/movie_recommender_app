from flask import Flask, Response, request, jsonify, render_template, url_for
from movierecommenderpackage.utils import movies, lookup_movie, movie_genres, genres
from movierecommenderpackage.recommender import neighbor_recommender, nmf_recommender


# here we construct a Flack object and the __name__ sets this script as the root
app = Flask(__name__)

# a python decorator for defining a mapping between a url and a function
@app.route('/')
def homepage():
    print(genres)
    return render_template('homepage.html', genres=genres)

# dynamic parametrized endpoint
@app.route('/movies/<int:movieId>')
def movie_info(movieId):
    try:
        movie=movies.loc[movieId].to_dict()
        return render_template('movie_info.html', movie=movie)
    except KeyError:
        # return Response(status=404)
        return 'movie id does not exist!'


@app.route('/movies/search')
def movie_search():
    # QUERY STRINGS: https://en.wikipedia.org/wiki/Query_string

    # ?q=titanic&q=indiana%20jones&q=star%20wars
    # print(request.args.getlist('q'))
    
    # ?q=titanic
    query = request.args.get('q')
    results = lookup_movie(query, movies['title'])
    return render_template('movie_search.html', results=results)


@app.route('/movies/recommend')
def recommend():
    print(request.args)
    # recommend_most_popular(movie_average_rating)
    movie=request.args.getlist('movie')
    while '' in movie:
        movie.remove('')
    rating=request.args.getlist('rating')
    while '' in rating:
        rating.remove('')   
    genre=request.args.getlist('genre')
    user_ratings = dict(zip(movie,rating))
    user ={
        'ratings':user_ratings,
        'genres':genre
    }
    recommender=request.args.getlist('recommender')
    print(recommender)

    if not recommender:
        recommendations = neighbor_recommender(user)
    else:
        if recommender[0]=='neighbor':
            recommendations = neighbor_recommender(user)
        if recommender[0]=='nmf':
            recommendations = nmf_recommender(user) 


    print(recommendations)


    # here would be a great place to use your recommender function
    # rec = recommend_random([3,45]) then pass rec=rec to recommend.html
    return render_template('recommend.html', 
                            movie=movie, 
                            rating=rating, 
                            genre=genre,
                            new_user=user,
                            recommendations=recommendations,
                            recommender=recommender)




if __name__ == "__main__":
    # runs app and debug=True ensures that when we make changes the web server restarts
    app.run(debug=True)
