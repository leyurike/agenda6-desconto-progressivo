# Sistema de desconto progressivo para loja online
 
# --- ENTRADA ---
# Solicita ao usuário o valor total da compra e converte para número decimal (float)
valor_compra = float(input("Digite o valor total da compra: R$ "))
 
# --- PROCESSAMENTO ---
# Estrutura condicional (if/elif/else) que define o percentual de desconto
# de acordo com a faixa de valor da compra
if valor_compra < 200:
    percentual_desconto = 0.05  # 5% de desconto
elif valor_compra < 300:
    percentual_desconto = 0.10  # 10% de desconto
else:
    percentual_desconto = 0.15  # 15% de desconto
    
# Calcula o valor do desconto e o valor final a ser pago
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# --- SAÍDA ---
# Exibe o percentual aplicado, o valor do desconto e o valor final a pagar
print(f"Percentual de desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
 