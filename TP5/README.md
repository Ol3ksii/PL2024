# TPC5

**Author**: [**A102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 2025-03-16

## Summary

In this task (TPC5), the goal is to develop a Python program that simulates a vending machine.

The program must:

- **Maintain stock management** using a JSON file (`stock.json`) to store product details persistently.
- **Process user commands** such as:
  - **LISTAR**: Display available products.
  - **MOEDA**: Insert money in various denominations.
  - **SELECIONAR <cod>**: Select and purchase a product.
  - **ADICIONAR <cod> "nome" <quant> <preco>**: Add or update a product.
  - **SAIR**: Exit and return change if applicable.
- **Handle error cases** such as insufficient stock, invalid commands, and incorrect input formats.

## Results

The program is executed from the command line and maintains the stock between sessions. Example usage:

```bash
python3 TPC5.py
```

## stock.json:
```json
[
    { "cod": "B10", "nome": "Café Expresso", "quant": 15, "preco": 1.0 },
    { "cod": "B11", "nome": "Chá Verde", "quant": 8, "preco": 1.2 },
    { "cod": "B12", "nome": "Sumo de Laranja 250ml", "quant": 6, "preco": 1.5 },
    { "cod": "B13", "nome": "Barra de Cereais", "quant": 10, "preco": 0.9 },
    { "cod": "B14", "nome": "Bolacha de Chocolate", "quant": 12, "preco": 1.3 }
]
```

## Example Interaction:
```
maq: 2025-03-08, Stock carregado. Máquina pronta.
>> LISTAR
maq:
cod  | nome               | quantidade | preço
----------------------------------------------
B10  | Café Expresso      | 15         | 1.0
B11  | Chá Verde          | 8          | 1.2
B12  | Sumo de Laranja 250ml | 6          | 1.5
B13  | Barra de Cereais   | 10         | 0.9
B14  | Bolacha de Chocolate | 12         | 1.3

>> MOEDA 1e 50c 20c.
maq: Saldo = 170c

>> SELECIONAR B10
maq: Pode retirar o produto dispensado "Café Expresso"
maq: Saldo = 70c

>> SELECIONAR B10
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 70c; Pedido = 100c

>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c.
maq: Até à próxima
```

- **1** (Stock management):
    ```
    LISTAR
    ```
    Displays the available products and their stock levels.

- **2** (Money insertion and balance update):
    ```
    MOEDA 1e 50c 20c
    ```
    Updates the balance accordingly.

- **3** (Product selection and purchase):
    ```
    SELECIONAR B10
    ```
    Dispenses the product if the balance is sufficient.

- **4** (Handling insufficient balance):
    ```
    SELECIONAR B10
    ```
    Prevents purchase if funds are insufficient.

- **5** (Returning change and exiting):
    ```
    SAIR
    ```
    Provides the correct change before terminating.

## Conclusion

The vending machine simulator successfully processes user commands, manages stock dynamically, handles transactions, and ensures data persistence using JSON. The implementation provides an interactive experience while providing error handling for a realistic vending machine simulation.