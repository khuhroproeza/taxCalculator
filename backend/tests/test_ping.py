from tests.conftest import client
import json
from datetime import datetime


def test_item_type_analyser():
    query = "itemInput=chocolates"
    response = client.get(f"taxCal?{query}")
    assert response.status_code == 200
    assert response.json() == {"item": "food"}


def test_post_get_receipt():
    order_list = json.dumps(
        {
            "item": "books",
            "Itemtype": "books",
            "TaxType": "imported_item",
            "quantity": 1,
            "price": 10.54,
        }
    )
    response = client.post("taxCal", data=order_list)
    assert response.status_code == 200
    response_item = response.json()
    del response_item["id"]
    del response_item["created_at"]
    assert response_item == {
        "item": "books",
        "Itemtype": "books",
        "TaxType": "imported_item",
        "quantity": 1,
        "price": 10.54,
        "total": 11.09,
        "tax": 0.55,
    }
