from typing import Any
from typing import Dict
from typing import List
from typing import Type

from fastapi import Depends

from dao import WalletDAO
from models import Account
from models import Wallet


class WalletService:

    def __init__(self, wallet_dao=Depends(WalletDAO)):
        self.wallet_dao = wallet_dao

    def get_wallet_by_id(self, wallet_id: int) -> Type[Wallet]:
        return self.wallet_dao.get_wallet_by_id(wallet_id)

    # notice how return type is List[Type[Account]] regardless of if we want the simple or the extended result
    # presentational logic is decoupled and is the responsibility of the DTO
    def get_accounts_by_wallet_id(self, wallet_id: int, extended: bool = False) -> List[Type[Account]]:
        if extended:
            return self.wallet_dao.get_accounts_by_wallet_id_extended(wallet_id)
        else:
            return self.wallet_dao.get_accounts_by_wallet_id(wallet_id)

    def get_accounts_per_symbol(self, wallet_id: int) -> List[Dict[str, Any]]:
        return self.wallet_dao.get_accounts_per_symbol(wallet_id)
