from flask import render_template, request, redirect, url_for
from . import main
# from .. requests import 
# from .forms import ReviewForm
from ..sources_model import Display
from ..articles_model import Display

@main.route('/')
def index():

    message = "We made it Mama"
    return render_template('index.html', message = message)