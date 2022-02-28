import unittest
from app.sources_model import Sources

class SourcesTest(unittest.TestCase):

    def setUP(self):
        self.new_source = Sources(74,'New York Times','https://www.engadget.com/netflix-billion-dollar-bitcoin-launderers-192241113.html','Motivation', 'English', 'USA' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))