from fastapi import FastAPI


app = FastAPI()


vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

@app.get("/")
def home ():
    return {"Venda": len(vendas)}


@app.get("/vendas/{venda_id}")
def pegar_vendas(venda_id: int):
    return vendas[venda_id]
  