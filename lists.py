yes_words = [

    "yes", "y", "ye", "yeah", "yep", "ya", "yup", "sure", "ok", "okay", "affirmative", "of course", "certainly", "definitely",
    "positive", "absolutely", "indeed", "roger", "aye", "totally", "yessir", "yessirrr", "yass", "yas", "yees", "yessir", "yasss",
    "y3s", "yeaah", "yeh", "yahs", "yassir", "yassirrr", "yassirrrr", "yassirrrrr", "yassirrrrrr",
    # common typos
    "yse", "eys", "yea", "ys", "yess", "yesss", "yup", "yessir", "yass", "yas", "yees", "yessir", "yasss"
]
cards = [
    rank + suit
    for suit in ['♠', '♥', '♦', '♣']
    for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
]

dealer_quotes = [
    "get even... or get even worse",
    "play suited trash",
    "does anyone even know how to play omaha?",
    "dont worry, I'm shuffling with my eyes closed",
]

call_typos = [
    "call", "Call", "CALL", "c", "C"
]

check_typos = [
    "check", "Check", "CHECK", "ch", "Ch", "CH", "chek", "chekc", "checl", "checc", "chek", "cek", "k", "K"
]

raise_typos = [
    "raise", "Raise", "RAISE", "r", "R", "raize", "raze", "rais", "raiae", "raies", "raisr", "rause"
]

fold_typos = [
    "fold", "Fold", "FOLD", "f", "F", "fole", "fol", "fodl", "fild", "folds", "foldd", "f0ld", "fo1d"
]