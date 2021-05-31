import json
def store_data_import():
    my_json_string = """{
        "store_details": 
        {
            "seller_name":"משה כהן",
            "store_id": "34821",
            "store_address": "החשמונאים 18",
            "store_city": "תל אביב",
            "store_name": "הום סנטר",
            "store_phone": "1800756123",
            "category":"בית וגן"
        },
        
        "purchase_details": 
        {
            "payment_type": "אשראי",
            "credit_number": 1095,
            "vat": 0.17,
            "warranty": 0,
            "payments": 3
        }
         
    }
    """
    return json.loads(my_json_string)


