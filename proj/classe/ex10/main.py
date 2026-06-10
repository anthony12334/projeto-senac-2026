from carrinho import CarrinhoDeCompras
if__name__ == "__main__"
meu_carrinho = CarrinhoDeCompras()

meu_carrinho.adicionar_itens(bazuca, 100,00)
meu_carrinho.adicionar_itens(coluna, 99,90)
meu_carrinho.adicionar_itens(ak47, 19,90)

total = meu_carrinho.calcular_tudo()
print(f"itens no carrinho:){meu_carrinho.itens}")
print (f"valor total foi R$ {total:}")
