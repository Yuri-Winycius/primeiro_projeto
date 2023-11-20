from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {'item': 'Lata', 'preco': 4, 'quantidade': 5},
    2: {'item': 'garrafa', 'preco': 8, 'quantidade': 2},
    3: {'item': 'caixinha', 'preco': 2, 'quantidade': 7},
}

@app.get('/')
def home():
    return {'Vendas': len(vendas)}

@app.get('/vendas/{id_venda}')
def pegar_venda(id_venda: int):
    return vendas[id_venda]