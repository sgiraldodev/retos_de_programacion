from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Customer(BaseModel):
    identification: str
    name: str 
    email: EmailStr
    description: Optional[str] = None
    city: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CustomerCreate(Customer):
    pass #Saltamos la validacion del codigo temporalmente
    id: Optional[int] = None
    

class Transaction(BaseModel):
    id:int
    amount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer:Customer
    transactions:list[Transaction]
    amount_total:int

@property
def ammount_total(self):
    return sum(transaction.amount for transaction in self.transactions)


class Config:
    orm_mode = True