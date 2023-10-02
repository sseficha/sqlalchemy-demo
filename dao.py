from typing import Any
from typing import Dict
from typing import List
from typing import Type

from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from database import get_session
from models import Account
from models import Currency
from models import Wallet


class WalletDAO:

    def __init__(self, session=Depends(get_session)):
        self.session = session

    def get_wallet_by_id(self, wallet_id: int) -> Type[Wallet]:
        wallet = self.session.query(Wallet).where(Wallet.id == wallet_id).limit(1).first()
        if wallet:
            return wallet
        else:
            raise HTTPException(status_code=404, detail=f"Wallet with id: {wallet_id} doesn't exist")

    def get_accounts_by_wallet_id(self, wallet_id: int) -> List[Type[Account]]:
        wallet = self.get_wallet_by_id(wallet_id)  # accounts are not yet loaded as they are lazy
        return wallet.accounts  # now the wallet's accounts get instantiated (select query is run)

    def get_accounts_by_wallet_id_extended(self, wallet_id: int) -> List[Type[Account]]:
        # eager load currency from the beginning
        return self.session.query(Account) \
            .options(joinedload(Account.currency, innerjoin=True)) \
            .where(Account.master_account == wallet_id).all()

    # if this is too pythonic for you sqlalchemy allows for textual representation as well
    def get_accounts_per_symbol(self, wallet_id: int) -> List[Dict[str, Any]]:
        res = self.session.query(Currency.symbol, func.count(Account.id)) \
            .join(Account) \
            .where(Account.master_account == wallet_id) \
            .group_by(Currency.symbol).all()
        return [{"symbol": row[0], "count": row[1]} for row in res]
