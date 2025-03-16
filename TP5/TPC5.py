#!/usr/bin/env python3
import json
import os
from datetime import date

STOCK_FILE = "stock.json"

def load_stock():
    if not os.path.exists(STOCK_FILE):
        return []
    with open(STOCK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, ensure_ascii=False, indent=2)

def find_product(stock, cod):
    for p in stock:
        if p["cod"].upper() == cod.upper():
            return p
    return None

def listar(stock):
    if not stock:
        print("maq: [Stock vazio]")
        return
    print("maq:\ncod  | nome               | quantidade | preço")
    print("----------------------------------------------")
    for p in stock:
        cod = p["cod"]
        nome = p["nome"]
        quant = p["quant"]
        preco = p["preco"]
        print(f"{cod:<4} | {nome:<18} | {quant:<10} | {preco}")

def inserir_moedas(line, balance):
    coins_str = line.split()[1:]
    for coin_str in coins_str:
        coin_str = coin_str.strip().lower().replace(".", "")
        if coin_str.endswith("e"):
            try:
                euros = int(coin_str[:-1])
                balance += euros * 100
            except ValueError:
                pass
        elif coin_str.endswith("c"):
            try:
                cents = int(coin_str[:-1])
                balance += cents
            except ValueError:
                pass
    return balance

def selecionar(stock, cod, balance):
    produto = find_product(stock, cod)
    if not produto:
        print(f"maq: Produto '{cod}' não existe.")
        return balance
    preco = int(round(produto["preco"] * 100))
    if produto["quant"] < 1:
        print("maq: Produto sem stock.")
        return balance
    if balance < preco:
        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
        print(f"maq: Saldo = {balance}c; Pedido = {preco}c")
        return balance
    produto["quant"] -= 1
    balance -= preco
    print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
    print(f"maq: Saldo = {balance}c")
    return balance

def calcular_troco(balance):
    troco = []
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    for m in moedas:
        if balance <= 0:
            break
        qtd = balance // m
        if qtd > 0:
            troco.append((m, qtd))
            balance -= m * qtd
    return troco

def adicionar(stock, line):
    parts = line.strip().split(maxsplit=4)
    if len(parts) < 5:
        print("maq: Uso: ADICIONAR <cod> <nome entre aspas> <quant> <preco>")
        return
    _, cod, rest = parts[0], parts[1], parts[2:]
    temp_str = " ".join(rest)
    primeira = temp_str.find('"')
    segunda = temp_str.find('"', primeira+1)
    if primeira == -1 or segunda == -1:
        print("maq: Falha ao ler o nome do produto")
        return
    nome = temp_str[primeira+1:segunda]
    depois_nome = temp_str[segunda+1:].strip()
    partes_2 = depois_nome.split()
    if len(partes_2) < 2:
        print("maq: Falta quantidade/preço")
        return
    try:
        quant = int(partes_2[0])
        preco = float(partes_2[1])
    except:
        print("maq: Formato de quantidade/preço inválido")
        return
    existente = find_product(stock, cod)
    if existente:
        existente["nome"] = nome
        existente["quant"] += quant
        existente["preco"] = preco
        print(f"maq: Produto '{cod}' atualizado. Quantidade acrescida de {quant}.")
    else:
        novo = {"cod": cod, "nome": nome, "quant": quant, "preco": preco}
        stock.append(novo)
        print(f"maq: Produto '{cod}' adicionado ao stock.")

def main():
    stock = load_stock()
    print(f"maq: {date.today()}, Stock carregado. Máquina pronta.")
    balance = 0
    while True:
        try:
            line = input(">> ").strip()
        except EOFError:
            line = "SAIR"
        if not line:
            continue
        cmd = line.split()[0].upper()
        if cmd == "LISTAR":
            listar(stock)
        elif cmd == "MOEDA":
            balance = inserir_moedas(line, balance)
            print(f"maq: Saldo = {balance}c")
        elif cmd == "SELECIONAR":
            if len(line.split()) < 2:
                print("maq: Uso: SELECIONAR <cod>")
            else:
                cod = line.split()[1]
                balance = selecionar(stock, cod, balance)
        elif cmd == "ADICIONAR":
            adicionar(stock, line)
        elif cmd == "SAIR":
            if balance > 0:
                troco = calcular_troco(balance)
                if troco:
                    troco_str = []
                    for (m, qtd) in troco:
                        if m >= 100:
                            troco_str.append(f"{qtd}x {m//100}e")
                        else:
                            troco_str.append(f"{qtd}x {m}c")
                    print(f"maq: Pode retirar o troco: {', '.join(troco_str)}.")
            print("maq: Até à próxima")
            save_stock(stock)
            break
        else:
            print("maq: Comando inválido")

if __name__ == "__main__":
    main()
