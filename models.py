from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import Base


class Wallet(Base):
    # configuration
    __tablename__ = "main"
    __table_args__ = {"schema": "hfdbpk"}

    # mapped columns
    id: Mapped[int] = mapped_column(name='id', primary_key=True)
    first_name: Mapped[str] = mapped_column(name="fname")
    last_name: Mapped[str] = mapped_column(name="lname")
    country: Mapped[str] = mapped_column(name="country")
    phone: Mapped[str] = mapped_column(name="phone")
    email: Mapped[str] = mapped_column(name="email")
    password: Mapped[str] = mapped_column(name="password")

    # relationships
    accounts: Mapped[List["Account"]] = relationship(back_populates="wallet", lazy="selectin")

    # string representation
    def __repr__(self) -> str:
        return f"Wallet(id={self.id}, " \
               f"first_name={self.first_name}, " \
               f"last_name={self.last_name}, " \
               f"country={self.country}, " \
               f"phone={self.phone}, " \
               f"email={self.email}, " \
               f"password={self.password})"


class Account(Base):
    __tablename__ = "accounts"
    __table_args__ = {"schema": "hfdbpk"}

    id: Mapped[int] = Column(name="mt4account", primary_key=True)
    cc: Mapped[str] = mapped_column(name="cc")
    type: Mapped[str] = mapped_column(name="acc_type")
    demo_live: Mapped[str] = mapped_column(name="demo_live")
    master_account = mapped_column(ForeignKey("hfdbpk.main.id"))
    currency_iso = mapped_column(ForeignKey("housekeeping.h_currencies.currency_iso"), name="currency")

    wallet: Mapped[Wallet] = relationship(back_populates="accounts")
    currency: Mapped["Currency"] = relationship()

    def __repr__(self) -> str:
        return f"Account(id={self.id}, " \
               f"cc={self.cc}, " \
               f"type={self.type}," \
               f"demo_live={self.demo_live})"


class Currency(Base):
    __tablename__ = "h_currencies"
    __table_args__ = {"schema": "housekeeping"}

    id: Mapped[int] = Column(name="id", primary_key=True, autoincrement=True)
    currency_iso: Mapped[str] = Column(name="currency_iso")
    name: Mapped[str] = Column(name="name")
    symbol: Mapped[str] = Column(name="currency_symbol")

    def __repr__(self) -> str:
        return f"Currency(id={self.id}, " \
               f"currency_iso={self.currency_iso}, " \
               f"name={self.name}, " \
               f"symbol={self.symbol})"
