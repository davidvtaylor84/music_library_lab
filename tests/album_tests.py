import unittest
from models.album import Album

class TestTask(unittest.TestCase):

    def setUp(self):
        self.album = Album("Daydream Nation", "Sonic Youth")

    def test_album_has_name(self):
        self.assertEqual("Daydream Nation", self.album.album_name)

    def test_album_has_artist(self):
        self.assertEqual("Sonic Youth", self.album.artist)