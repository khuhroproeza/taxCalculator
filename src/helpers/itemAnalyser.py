import difflib

food = [
    "Cheese",
    "chocolate",
    "chocolates",
    "Egg",
    "Butter",
    "Margarine",
    "Yogurt",
    "Cottage cheese",
    "Ice cream",
    "Cream",
    "Sandwich",
    "Sausage",
    "Hamburger",
    "Hot dog",
    "Bread",
    "Pizza",
    "Steak",
    "Roast chicken",
    "Fish",
    "Seafood",
    "Ham",
    "Kebab",
    "Bacon",
    "Sour cream",
]


medical = [
    "Solution",
    "Oral rinse",
    "headache pills",
    "Cough syrup",
    "Antiseptic",
    "Lotion",
    "Decongestant spray",
    "Softgel",
    "Blood",
    "Ointment",
    "Lozenges",
    "Powder",
    "pills",
    "pill," "Eye drops",
    "Effervescent tablet",
    "Tablet",
    "Toothpaste",
    "Aspirin",
    "Caplet",
    "Capsule",
]
books = [
    "book",
    "books",
    "notepad",
    "notebook",
    "pad",
    "memo pad",
    "exercise book",
    "binder" "ledger",
    "record book",
    "log",
    "logbook",
    "chronicle",
    "journal",
    "diary",
    "daybook",
]
item_types = {"food": food, "books": books, "medical": medical}


def find_item_type(string):
    score = 0
    item_return = None
    a = string
    for itemName, itemtype in item_types.items():
        for item in itemtype:
            b = item
            seq = difflib.SequenceMatcher(None, a, b)
            d_score = seq.ratio() * 100
            if d_score > score:
                score = d_score
                item_return = itemName
    if score < 60:
        item_return = "other"
    return item_return
