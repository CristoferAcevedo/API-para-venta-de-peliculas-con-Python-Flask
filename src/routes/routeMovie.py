from flask import Blueprint, jsonify,request

#modelos
from models.movieModel import MovieModel

main=Blueprint('route_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies=MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/<id>')
def get_movie(id):
    try:
        movie=MovieModel.get_movie(id)
        if movie == None:
            return jsonify({}),404
        
        return jsonify(movie)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add',methods=['POST'])
def add_movie():
    try:

        
        movie=MovieModel.add_movie(movie)
        if movie == None:
            return jsonify({}),404
        
        return jsonify(movie)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500