from flask import Flask
from config import config
from flask_cors import CORS

#rutas
from routes import routeMovie

app=Flask(__name__)

CORS(app,resources={"*":{"origins":"http://localhost:5173"}})

def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404

if __name__ =="__main__":
    app.config.from_object(config['development'])
    
    #registro de blueprint(rutas)
    app.register_blueprint(routeMovie.main, url_prefix='/api/movies')
    
    #manejo de errores
    app.register_error_handler(404,page_not_found)

    #ejecuta la app
    app.run()