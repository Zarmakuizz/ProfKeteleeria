# identify.test.py

import unittest
from src.search import Search
from src.card import Card

# Pour la détection de cartes : 
# - avoir une mini-bdd de test (qq listes en vrac au début suffiront)
# - la recherche trouve [Jirachi] (parmi 1)
# - la recherche trouve [Jirachi] (parmi 2+, prend le plus récent en date)
# - la recherche trouve [Jirachi SM9] (abréviation de série du site officiel, que je pomperai automatiquement de temps en temps)
# - la recherche trouve [Jirachi SM0 99] 
# - Support de plusieurs abréviations de série: Duo de chocs = SM9 et TEU
# - Support des suffixes (EX, GX, etc)
# - Support des noms composés (Pikachu & Zekrom GX, 42 façons différentes de l'écrire)
# - Support des noms incomplets : [Jirach] => [Jirachi]
# - Cas d'erreur : carte non identifiée

# Optionnel :
# - Support de plusieurs abréviations de série: Duo de chocs = SM9, SM09, TEU, TUP, DDC... (avec un cas de collision)
class TestSearch(unittest.TestCase):
    
    def test_get_jirachi(self): 
        # Arrange
        engine = Search()
        # TODO initialize BDD
        text = "[Jirachi]"

        # Act
        matches = engine.find_cards(text)

        # Assert
        self.assertTrue( len(matches) > 0)
        self.assertNotEqual("Jirachi", matches[0], "Retrieve a card instead")
        self.assertEqual("Jirachi", matches[0].name, "Card name should match")




if __name__ == '__main__':
    unittest.main()