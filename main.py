from typing import List

from fastapi import Depends
from fastapi import FastAPI

from dto import AccountDTO
from dto import AccountToSymbolDTO
from dto import ExtendedAccountDTO
from dto import WalletDTO
from services import WalletService

app = FastAPI()


@app.get("/wallets/{wallet_id}", response_model=WalletDTO)
def get_wallet(wallet_id: int, wallet_service=Depends(WalletService)):
    return wallet_service.get_wallet_by_id(wallet_id)


@app.get("/wallets/{wallet_id}/accounts", response_model=List[AccountDTO])
def get_accounts(wallet_id: int, wallet_service=Depends(WalletService)):
    return wallet_service.get_accounts_by_wallet_id(wallet_id)


@app.get("/wallets/{wallet_id}/accounts-extended", response_model=List[ExtendedAccountDTO])
def get_accounts(wallet_id: int, wallet_service=Depends(WalletService)):
    return wallet_service.get_accounts_by_wallet_id(wallet_id, extended=True)


@app.get("/wallets/{wallet_id}/accounts-per-symbol", response_model=List[AccountToSymbolDTO])
def get_accounts_per_symbol(wallet_id: int, wallet_service=Depends(WalletService)):
    return wallet_service.get_accounts_per_symbol(wallet_id)
