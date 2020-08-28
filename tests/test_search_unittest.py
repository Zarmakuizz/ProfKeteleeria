# identify.test.py

import unittest
from src.search import Search
from src.card import Card
from tests.fake_database import FakeDatabase 

class TestSearch(unittest.TestCase):
    cards = [
        Card("Jirachi"),
        Card("Pikachu"),
        Card("Jirachi"),
        Card("Jirachi {*}"),
        Card("Pikachu GX"),
        Card("Pikachu EX"),
        Card("Pikachu&Zekrom GX"),
        Card("Intelleon V"),
        Card("Intelleon Vmax"),
    ]
    
    def test_get_jirachi(self): 
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirachi]"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertTrue( len(matches) > 0)
        self.assertNotEqual("Jirachi", matches[0], "Retrieve a card instead")
        self.assertEqual("Jirachi", matches[0].name, "Card name should match")
    
    def test_get_incomplete_name(self): 
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirach]"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertTrue( len(matches) > 0)
        self.assertEqual("Jirachi", matches[0].name, "Incomplete text should be enough to retrieve a card")

    def test_get_none(self): 
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Kuriboh]"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertTrue( len(matches) > 0, "We always return a card object")
        result = matches[0]
        self.assertFalse( result.is_valid(), "No Pokémon card should have that name")
    
    def test_get_last_jirachi(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirachi]"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertFalse( matches, "we lack any information on card's release date")
    
    def test_get_jirachi_by_series(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirachi]"
        series = "SM9"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertFalse( matches, "we lack any information on card's series")
    
    def test_get_jirachi_by_alternative_series(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirachi]"
        series1 = "SM9"
        series2 = "TEU"
        series3 = "SM09"

        # Act
        matches1 = engine.find_cards(text) # TODO use series1
        matches2 = engine.find_cards(text) # TODO use series2
        matches3 = engine.find_cards(text) # TODO use series3

        # Assert
        self.assertEqual( matches1[0], matches2[0], "Pokemon.com abbreviation and tournament official abbreviation should match")
        self.assertEqual( matches1[0], matches3[0], "Pokemon.com abbreviation and Pokécardex abbreviation should match")
    
    def test_get_jirachi_by_series_and_number(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text = "[Jirachi]"
        series = "SM9"
        number = 99

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertFalse( matches, "we lack any information on card's series and #")
    
    def test_get_GX_card(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text1 = "[Pikachu GX]"
        text2 = "[Pikachu-GX]"

        # Act
        matches1 = engine.find_cards(text1)
        matches2 = engine.find_cards(text2)

        # Assert
        self.assertEqual(matches1[0].name, matches2[0].name, "Should be the same card")
    
    def test_get_EX_card(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text1 = "[Pikachu EX]"
        text2 = "[Pikachu-EX]"

        # Act
        matches1 = engine.find_cards(text1)
        matches2 = engine.find_cards(text2)

        # Assert
        self.assertEqual(matches1[0].name, matches2[0].name, "Should be the same card")
    
    def test_get_V_card(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text1 = "[Intelleon V]"
        text2 = "[Intelleon-V]"

        # Act
        matches1 = engine.find_cards(text1)
        matches2 = engine.find_cards(text2)

        # Assert
        self.assertEqual(matches1[0].name, matches2[0].name, "Should be the same card")
        self.assertNotIn("Vmax", matches1[0].name, "Should not pick the Vmax card")
    
    def test_get_Vmax_card(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text1 = "[Intelleon Vmax]"
        text2 = "[Intelleon-Vmax]"

        # Act
        matches1 = engine.find_cards(text1)
        matches2 = engine.find_cards(text2)

        # Assert
        self.assertEqual(matches1[0].name, matches2[0].name, "Should be the same card")
        self.assertNotEqual(matches1[0].name, "Intelleon V" , "Should not pick the V card")

    def test_get_Tag_Team_card(self):
        # Arrange
        db = FakeDatabase(self.cards)
        engine = Search(db)
        text1 = "[Pikachu&Zekrom GX]"
        text2 = "[Pikachu Zekrom]"
        text3 = "[Pikachu & Zekrom]"

        # Act
        matches1 = engine.find_cards(text1)
        matches2 = engine.find_cards(text2)
        matches3 = engine.find_cards(text3)

        # Assert
        self.assertEqual(matches1[0].name, matches2[0].name, "Should be the same card")
        self.assertEqual(matches1[0].name, matches3[0].name, "Should be the same card")


if __name__ == '__main__':
    unittest.main()