from dataclasses import dataclass
from typing import Optional


@dataclass
class AccountRequest:
    name: str
    type: str
    balance: int
