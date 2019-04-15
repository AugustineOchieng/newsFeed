class Config:
  NEW_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
class ProdConfig(Config):
  pass
class DevConfig(Config):
  DEBUG = True