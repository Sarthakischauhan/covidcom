from app import user
from flask import Flask
import os 
from flask_googlemaps import GoogleMaps



app = Flask(__name__)
GoogleMaps(app=app)

if app.config["ENV"]=="development":
	app.config.from_object("config.DevelopmentConfig")
	app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
	app.config["GOOGLEMAPS_KEY"] = os.environ.get("GOOGLEMAPS_KEY")


from app.user.routes import users_bp

app.register_blueprint(users_bp)