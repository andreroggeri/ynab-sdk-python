from dataclasses import dataclass
from typing import Optional


@dataclass
class TransactionRequest:
    account_id: str
    date: str
    amount: int
    payee_id: Optional[str] = None
    payee_name: Optional[str] = None
    category_id: Optional[str] = None
    memo: Optional[str] = None
    cleared: Optional[str] = None
    approved: Optional[bool] = None
    flag_color: Optional[str] = None
    import_id: Optional[str] = None
