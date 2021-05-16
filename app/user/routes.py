from flask import Blueprint,request,render_template,session
from app.user.utils import *


users_bp = Blueprint("routes",__name__)

@users_bp.route("/")
def home():
    # lat,long=request.cookies.values()
    # address = loctoAddress(lat,long)["address"]
    # state,district = address["state_district"],address["state"]
    vac_link = getvaclink()
    return render_template("map.html",vac_link=vac_link)


@users_bp.route("/addLink",methods=["GET","POST"])
def add_link():
    type_ = request.args.get("type","vaccine")
    return render_template("add-link.html",type_=type_)
