from flask import render_template, Request, redirect, url_for
from .import main
from ..request import get_articles, get_news


#views
@main.route('/')
def index():
    """
    view root page that returns the index page and its related data
    """
    title = "Home  || News sources"
    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    sci_news = get_news('science')

    #print all news
    return render_template('index.html', title= title, sports= all_news,general= general_news, technology = tech_news, business = bus_news, science = sci_news)

#views
@main.route('/news/<int:id>')
def news(id):
    """
    view movie page function that returns the movie details page and its data
    """
    news = get_news(id)

    return render_template('index.html',news = news)
    