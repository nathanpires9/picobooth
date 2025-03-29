from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/photo-booth')
def photobooth():
    return render_template("photo-booth.html")

@views.route('/more-info')
def moreinfo():
    return render_template("more-info.html")

@views.route('/support')
def support():
    return render_template("support.html")

@views.route('/requests')
def requests():
    return render_template("requests.html")