from app import user
from flask import Flask
import os 



app = Flask(__name__)

if app.config["ENV"]=="development":
	app.config.from_object("config.DevelopmentConfig")
	# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


from app.user.routes import users_bp

app.register_blueprint(users_bp)