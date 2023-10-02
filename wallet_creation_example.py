from sqlalchemy.orm import Session

from database import engine
from models import Account
from models import Wallet

with Session(engine) as session:
    # create a wallet
    wallet = Wallet(id=12312,
                    first_name="Ted",
                    last_name="Mosbey",
                    country="Greece",
                    phone="6901010101",
                    email="tedmosbey@gmail.com",
                    password="SuperSecretPassword")
    session.add(wallet)

    # create an account
    account = Account(id=45645,
                      cc="0",
                      type="0",
                      demo_live="DEMO",
                      currency_iso="USD")

    # attach account to wallet
    wallet.accounts.append(account)

    # commit changes to db
    session.commit()

    print(wallet)
    print(wallet.accounts)
    print(wallet.accounts[0].currency)
