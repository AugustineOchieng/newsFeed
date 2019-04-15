from flask import render_template
from app import app
from .request import get_articles
@app.route('/')
def index():
  articles_name = get_articles('cnn') 
  return render_template('index.html', name = articles_name)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  return render_template('movie.html', id = movie_id)