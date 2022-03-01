from flask import render_template, request, redirect, url_for

from app.requests import get_by_category, get_source, getarticle_source
from . import main
from ..sources_model import Display
from ..articles_model import Display

@main.route('/')
def index():

    message = "We made it Mama"
    sources = get_source()
    return render_template('index.html', message = message, sources = sources)

@main.route('/article/<id>')
def article(id):

    article = getarticle_source(id)
    return render_template('article.html', id = id, article = article)

@main.route('/categories/<cat_name>')
def category(cate_name):

    category = get_by_category(cate_name)
    title = f'{cate_name}'
    cate = cate_name
    return render_template('category.html', title=title, category=category, cate=cate)
