import unittest
from models import movie
Article = article.Article

class ArticleTest(unittest.TestCase):
  def setUp(self):
    self.new_article = Artcle(null, "Accuweather.com", null, "Deadly tornado strikes Mississippi, bringing weekend death toll to 3 - AccuWeather.com", null, "https://www.accuweather.com/en/weather-news/live-deadly-tornado-strikes-mississippi-bringing-weekend-death-toll-to-4/70007983", null,
"2019-04-14T20:41:00Z", null)
  def test_instance(self):
    self.asserTrue(isinstance(self.new_movie, Movie))
if __name__ == '__main__':
  unittest.main()