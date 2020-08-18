VALID_BUDGETS = {
    "data": {
        "budgets": [
            {
                "id": "string",
                "name": "string",
                "last_modified_on": "2019-05-04T00:21:53.323Z",
                "first_month": "string",
                "last_month": "string",
                "date_format": {"format": "string"},
                "currency_format": {
                    "iso_code": "string",
                    "example_format": "string",
                    "decimal_digits": 0,
                    "decimal_separator": "string",
                    "symbol_first": True,
                    "group_separator": "string",
                    "currency_symbol": "string",
                    "display_symbol": True,
                },
            }
        ]
    }
}

VALID_BUDGET = {
    "data": {
        "budget": {
            "id": "string",
            "name": "string",
            "last_modified_on": "2019-05-04T00:22:42.764Z",
            "first_month": "string",
            "last_month": "string",
            "date_format": {"format": "string"},
            "currency_format": {
                "iso_code": "string",
                "example_format": "string",
                "decimal_digits": 0,
                "decimal_separator": "string",
                "symbol_first": True,
                "group_separator": "string",
                "currency_symbol": "string",
                "display_symbol": True,
            },
            "accounts": [
                {
                    "id": "string",
                    "name": "string",
                    "type": "checking",
                    "on_budget": True,
                    "closed": True,
                    "note": "string",
                    "balance": 0,
                    "cleared_balance": 0,
                    "uncleared_balance": 0,
                    "transfer_payee_id": "string",
                    "deleted": True,
                }
            ],
            "payees": [
                {
                    "id": "string",
                    "name": "string",
                    "transfer_account_id": "string",
                    "deleted": True,
                }
            ],
            "payee_locations": [
                {
                    "id": "string",
                    "payee_id": "string",
                    "latitude": "string",
                    "longitude": "string",
                    "deleted": True,
                }
            ],
            "category_groups": [
                {"id": "string", "name": "string", "hidden": True, "deleted": True}
            ],
            "categories": [
                {
                    "id": "string",
                    "category_group_id": "string",
                    "name": "string",
                    "hidden": True,
                    "original_category_group_id": "string",
                    "note": "string",
                    "budgeted": 0,
                    "activity": 0,
                    "balance": 0,
                    "goal_type": "TB",
                    "goal_creation_month": "string",
                    "goal_target": 0,
                    "goal_target_month": "string",
                    "goal_percentage_complete": 0,
                    "deleted": True,
                }
            ],
            "months": [
                {
                    "month": "string",
                    "note": "string",
                    "income": 0,
                    "budgeted": 0,
                    "activity": 0,
                    "to_be_budgeted": 0,
                    "age_of_money": 0,
                    "deleted": True,
                    "categories": [
                        {
                            "id": "string",
                            "category_group_id": "string",
                            "name": "string",
                            "hidden": True,
                            "original_category_group_id": "string",
                            "note": "string",
                            "budgeted": 0,
                            "activity": 0,
                            "balance": 0,
                            "goal_type": "TB",
                            "goal_creation_month": "string",
                            "goal_target": 0,
                            "goal_target_month": "string",
                            "goal_percentage_complete": 0,
                            "deleted": True,
                        }
                    ],
                }
            ],
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
                }
            ],
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
            "scheduled_transactions": [
                {
                    "id": "string",
                    "date_first": "string",
                    "date_next": "string",
                    "frequency": "never",
                    "amount": 0,
                    "memo": "string",
                    "flag_color": "red",
                    "account_id": "string",
                    "payee_id": "string",
                    "category_id": "string",
                    "transfer_account_id": "string",
                    "deleted": True,
                }
            ],
            "scheduled_subtransactions": [
                {
                    "id": "string",
                    "scheduled_transaction_id": "string",
                    "amount": 0,
                    "memo": "string",
                    "payee_id": "string",
                    "category_id": "string",
                    "transfer_account_id": "string",
                    "deleted": True,
                }
            ],
        },
        "server_knowledge": 0,
    }
}

VALID_SETTINGS = {
    "data": {
        "settings": {
            "date_format": {"format": "string"},
            "currency_format": {
                "iso_code": "string",
                "example_format": "string",
                "decimal_digits": 0,
                "decimal_separator": "string",
                "symbol_first": True,
                "group_separator": "string",
                "currency_symbol": "string",
                "display_symbol": True,
            },
        }
    }
}
