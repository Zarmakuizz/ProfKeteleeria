# identify.test.py

import unittest
from datetime import date
from src.search import Search
from src.card import Card
from src.error_card import ErrorCard
from src.series import Series
from tests.fake_database import FakeDatabase 

class TestSearch(unittest.TestCase):
    
    def test_get_jirachi(self): 
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Jirachi]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertEqual("Jirachi", match.name, "Card name should match")
    
    def test_get_incomplete_name(self): 
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Jirach]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertTrue("Jirachi" in match.name, "Incomplete text should be enough to retrieve a card")

    def test_get_none(self): 
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Kuriboh]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertIsInstance( match, Card, "We always return a card object")
        self.assertIsInstance( match, ErrorCard, "We return an Error object instead")
        self.assertFalse( match.is_valid(), "No Pokémon card should have that name")
    
    def test_get_last_jirachi(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Jirachi]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertEqual( match.series.name, "Team Up", "Oldest Jirachi is in Team Up")
    
    def test_get_jirachi_by_series(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Jirachi SM7]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertEqual( match.series.name, "Celestial Storm", "We requested Jirachi {*} from Celestial Storm")
    
    def test_get_jirachi_by_alternative_series(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Jirachi SM9]"
        text2 = "[Jirachi TEU]"
        text3 = "[Jirachi SM09]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]
        match3 = engine.find_cards(text3)[0]

        # Assert
        self.assertEqual( match1, match2, "Pokemon.com abbreviation and tournament official abbreviation should match")
        self.assertEqual( match1, match3, "Pokemon.com abbreviation and Pokécardex abbreviation should match")
    
    def test_get_jirachi_by_series_and_number(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text = "[Jirachi SM9 99]"

        # Act
        match = engine.find_cards(text)[0]

        # Assert
        self.assertEqual("Jirachi", match.name, "Card should be found")
        self.assertEqual("Team Up", match.series.name, "Card should have the right series")
        self.assertEqual(99, match.number, "Card should have the right collection number")
    
    def test_get_GX_card(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Pikachu GX]"
        text2 = "[Pikachu-GX]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]

        # Assert
        self.assertNotIsInstance( match1, ErrorCard, "Should find a card")
        # Beware of not picking Pikachu&Zekrom GX
        self.assertEqual(match1.name, "Pikachu GX", "The right card should be found")
        self.assertEqual(match1, match2, "Should be the same card")
    
    def test_get_EX_card(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Pikachu EX]"
        text2 = "[Pikachu-EX]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]

        # Assert
        self.assertNotIsInstance( match1, ErrorCard, "Should find a card")
        self.assertEqual(match1, match2, "Should be the same card")
    
    def test_get_V_card(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Inteleon V]"
        text2 = "[Inteleon-V]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]

        # Assert
        self.assertNotIsInstance( match1, ErrorCard, "Should find a card")
        self.assertEqual(match1, match2, "Should be the same card")
        self.assertNotIn("Vmax", match1.name, "Should not pick the Vmax card")
    
    def test_get_Vmax_card(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Inteleon Vmax]"
        text2 = "[Inteleon-Vmax]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]

        # Assert
        self.assertNotIsInstance( match1, ErrorCard, "Should find a card")
        self.assertEqual(match1, match2, "Should be the same card")
        self.assertNotEqual(match1.name, "Inteleon V" , "Should not pick the V card")

    def test_get_Tag_Team_card(self):
        # Arrange
        db = FakeDatabase()
        engine = Search(db)
        text1 = "[Pikachu&Zekrom GX]"
        text2 = "[Pikachu Zekrom]"
        text3 = "[Pikachu & Zekrom]"

        # Act
        match1 = engine.find_cards(text1)[0]
        match2 = engine.find_cards(text2)[0]
        match3 = engine.find_cards(text3)[0]

        # Assert
        self.assertNotIsInstance( match1, ErrorCard, "Should find a card")
        self.assertEqual(match1, match2, "Should be the same card")
        self.assertEqual(match1, match3, "Should be the same card")


    
    def test_get_by_french_name(self):
        # Arrange
        # db = FakeDatabase()
        # engine = Search(db)
        # text = "[Lézargus]"

        # # Act
        # match = engine.find_cards(text)[0]

        # # Assert
        # self.assertTrue("Inteleon" in match.name, "Inteleon is Lézargus in French")
        self.fail("Feature not supported with the fake database")


if __name__ == '__main__':
    unittest.main()