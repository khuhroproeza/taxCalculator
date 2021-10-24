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


def churn(num):
    num = str(num)
    num = list(num)
    add_digit = None
    length = len(num)
    while length >= 3:
        s = num[length - 1]
        if int(s) >= 5:
            num[length - 2] = str(int(num[length - 2]) + 1)
        length = length - 1
    num = num[:2]
    if len(num) > 1:
        if int(num[1]) >= 10:
            num[1] = "0"
            num[0] = str(int(num[0]) + 1)
        if int(num[1]) > 5:
            num[1] = "0"
            num[0] = str(int(num[0]) + 1)
        if int(num[0]) >= 10:
            add_digit = True
    num = int("".join(num))
    return num, add_digit


def proper_round(num):
    num = str(num).split(".")
    before = None
    if len(num) > 1:
        before = num[0]
        num = num[1]
    num = str(num)
    num = int("".join(num))
    num, add_digit = churn(num)
    if add_digit:
        before = str(int(before) + 1)
        num = 0
    final = float(before + "." + str(num))
    return float(str(round(round(final / 0.05) * 0.05, 2)))


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
