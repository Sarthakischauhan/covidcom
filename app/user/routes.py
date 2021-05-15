from flask import Blueprint,request,render_template,session
from app.user.utils import *


users_bp = Blueprint("routes",__name__)

@users_bp.route("/")
def home():
    lat,long=request.cookies.values()
    print(lat,long)
    return render_template("map.html")
