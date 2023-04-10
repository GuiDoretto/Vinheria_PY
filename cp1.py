#Mensagem de Boas Vindas.

print("Bem Vindo a Vinheria Agnello!")

#Cadastro.

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Voc� n�o tem idade suficiente para fazer uma compra de bebida alco�lica")
    exit()
endereco_cliente = input("Digite o seu endere�o para o cadastro: ")
endereco_entrega = input("Digite o endere�o que voc� quer que chegue a encomenda: ")

#Checar Idade.

if idade < 18:
    print("Voc� n�o possue idade suficiente para fazer compras de bebidas alcoolicas")
    exit()
else:

#Catalogo.

    catalogo = {
    "Merlot": 50.00,
    "Malbec": 60.00,
    "Prosecco": 70.00,
    "Syrah": 80.00,
    "Rioja": 90.00
}
#Pergunta quantos vinhos de cada.
total_pedido = 0.00
qtd_vinhos = {}

for vinho, preco in catalogo.items():
    qtd = int(input("Quantos vinhos de %s (R$%.2f) voc� deseja comprar? " % (vinho, preco)))
    total_vinho = qtd * preco
    qtd_vinhos[vinho] = qtd
    total_pedido += total_vinho

#Verifica o valor.

if total_pedido < 100.00:
    print("O valor m�nimo para compra � 100 Reais.")
    exit()

#Verifica se tem frete gratis.

if total_pedido > 200.00:
    frete = 0.00
    print("Voc� ganhou frete gratis!")

else:
    frete = 15.00

#Resumo
print("Resumo do pedido")
print("----------------")
for vinho, qtd in qtd_vinhos.items():
    print(f"{qtd} x {vinho}: R$ {catalogo[vinho] * qtd}")

print("----------------")
print(f"Total do pedido: R${total_pedido:.2f}")
print(f"Frete:{frete}")
pedido = total_pedido + frete
print(f"O total da compra: R${pedido}")
print(f"Endere�o da Entrega: {endereco_entrega}")
print("----------------")

#Confirma��o
confirma = input("Digite 'CONFIRMO' para autorizar o pedido: ")
if confirma == ("CONFIRMO"):
    print("Pedido conclu�do, Obrigado pela compra!")
else:
    print("Voc� cancelou o pedido.")