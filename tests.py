from main import generate_deck

def test_deckgeneration():
    deck = generate_deck()
    assert len(deck) == 52, "Should be 52"

if __name__ == "__main__":
    test_deckgeneration()
    print("Everything passed")