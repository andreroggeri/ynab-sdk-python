VALID_TRANSACTIONS = {
    "data": {
        "transactions": [
            {
                "id": "string",
                "date": "string",
                "amount": 0,
                "memo": "string",
                "cleared": "cleared",
                "approved": True,
                "flag_color": "red",
                "account_id": "string",
                "payee_id": "string",
                "category_id": "string",
                "transfer_account_id": "string",
                "transfer_transaction_id": "string",
                "matched_transaction_id": "string",
                "import_id": "string",
                "deleted": True,
                "account_name": "string",
                "payee_name": "string",
                "category_name": "string",
                "subtransactions": [
                    {
                        "id": "string",
                        "transaction_id": "string",
                        "amount": 0,
                        "memo": "string",
                        "payee_id": "string",
                        "category_id": "string",
                        "transfer_account_id": "string",
                        "deleted": True,
                    }
                ],
            }
        ],
        "server_knowledge": 0,
    }
}

VALID_TRANSACTION = {
    "data": {
        "transaction": {
            "id": "string",
            "date": "string",
            "amount": 0,
            "memo": "string",
            "cleared": "cleared",
            "approved": True,
            "flag_color": "red",
            "account_id": "string",
            "payee_id": "string",
            "category_id": "string",
            "transfer_account_id": "string",
            "transfer_transaction_id": "string",
            "matched_transaction_id": "string",
            "import_id": "string",
            "deleted": True,
            "account_name": "string",
            "payee_name": "string",
            "category_name": "string",
            "subtransactions": [
                {
                    "id": "string",
                    "transaction_id": "string",
                    "amount": 0,
                    "memo": "string",
                    "payee_id": "string",
                    "category_id": "string",
                    "transfer_account_id": "string",
                    "deleted": True,
                }
            ],
        }
    }
}
