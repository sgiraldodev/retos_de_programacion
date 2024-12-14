from fastapi import FastAPI
from models import Customer, Transaction, Invoice
import datetime

app = FastAPI(title="App para gestion de clientes y facturas")

@app.get("/", tags=["Main"], summary="Root Endpoint")
async def root():
    return {
        "message": "Bienvenido a la App para gestion de clientes y facturas",
        "hora": str(datetime.datetime.now())
    }

@app.post("/customers", tags=["Customers"], summary="Customers info")
async def customers(customer_data:Customer):
    return customer_data

@app.post("/transactons", tags=["Customers"], summary="Customers transactions")
async def transactions(transaction_data:Transaction):
    return transaction_data

@app.post("/invoices", tags=["Customers"], summary="Customer invoices")
async def invoices(invoice_data:Invoice):
    return invoice_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)