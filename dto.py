from pydantic import BaseModel


class WalletDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    country: str
    phone: str
    email: str

    # even though WalletDAO has password, DTO will be omitting it

    class Config:
        orm_mode = True


class AccountDTO(BaseModel):
    id: int
    cc: str
    type: str
    demo_live: str

    class Config:
        orm_mode = True
        

class CurrencyDTO(BaseModel):
    id: int
    currency_iso: str
    name: str
    symbol: str

    class Config:
        orm_mode = True


class ExtendedAccountDTO(AccountDTO):
    currency: CurrencyDTO


class AccountToSymbolDTO(BaseModel):
    symbol: str
    count: int
