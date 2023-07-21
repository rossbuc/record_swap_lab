from models.record import Record
import unittest

class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record("How High", "Cogniac", "Disco", "12\"")

    def test_record_has_title(self):
        self.assertEqual("How High", self.record.title)

    def test_record_has_artist(self):
        self.assertEqual("Cogniac", self.record.artist)

    def test_record_has_genre(self):
        self.assertEqual("Disco", self.record.genre)

    def test_record_has_format(self):
        self.assertEqual("12\"", self.record.format)