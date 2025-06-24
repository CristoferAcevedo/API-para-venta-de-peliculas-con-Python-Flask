from flask import Blueprint, jsonify,request
import uuid
#modelos
from models.movieModel import MovieModel

#Entities
from models.entities.Movie import Movie

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
        id = uuid.uuid4()
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']

        movie = Movie(str(id),title,duration,released)
        movie_añadida = MovieModel.add_movie(movie)

        if movie_añadida == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':'Error al insertar'}),500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/<id>',methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)

        movie_eliminada = MovieModel.delete_movie(movie)

        if movie_eliminada == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':'Error al eliminar'}),404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/update/<id>',methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']

        movie = Movie(id,title,duration,released)
        movie_modificada = MovieModel.update_movie(movie)

        if movie_modificada == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':'Error al modificar'}),500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500