from app import app
import urllib.request
import json
from .models import article

Article=article.Article

api_key = app.config['NEW_API_KEY']
base_url = app.config['ARTICLE_API_BASE_URL']
def get_articles(category):
  get_articles_url = base_url.format(category, api_key)
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)
    article_data = None
    if get_articles_response['articles']:
      article_results_list = get_articles_response['articles']
      article_results = process_results(article_results_list)
  return article_results
def process_results(article_list):
  article_results = []
  for article_item in article_list:
    id = article_item.get('id')
    name = article_item.get('name')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')
    if urlToImage:
      article_object = Article(id, name, author, title, description, url, urlToImage, publishedAt, content)
      article_results.append(article_object)
  return article_results