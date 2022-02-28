import unittest
from app.articles_model import Articles

class ArticlesTest(unittest.TestCase):

    def setUP(self):
        self.new_article = Articles(74,'New York Times', 'The Power of the Mind','https://s.yimg.com/os/creatr-uploaded-images/2022-02/74510970-89d5-11ec-bfaf-d4f39cae5191','Mark Me', '2022-02-11T19:22:41Z', 'There is no other powerful Body organ like the Brain' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))