import os

import os

os.system("cls" if os.name == "nt" else "clear")

print("""
====================MENU================
Código     Prato             Valor
----------------------------------------
1          Picanha           R$ 70.00
2          Lasanha           R$ 60.00
3          Strogonoff        R$ 50.00
4          Macarronada       R$ 42.00
5          Moqueca d' ovo    R$ 38.00
6          Cozido            R$ 35.00
7          Bolo d' pote      R$ 5.00
========================================
""")

def obter_preco(codigo):
    match codigo:
        case 1:
            return "Picanha", 70.00
        case 2:
            return "Lasanha", 60.00
        case 3:
            return "Strogonoff", 50.00
        case 4:
            return "Macarronada", 42.00
        case 5:
            return "Moqueca d' ovo", 38.00
        case 6:
            return "Cozido", 35.00
        case 7:
            return "Bolo d' pote", 5.00
        case _:
            return None, 0

def main():
    pedido = {}
    total = 0
    
    while True:
        try:
            codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))
            
            if codigo == 0:
                print("Pedido finalizado!")
                break
            
            nome_prato, preco = obter_preco(codigo)
            
            if nome_prato:
                if codigo in pedido:
                    pedido[codigo]['quantidade'] += 1
                else:
                    pedido[codigo] = {'nome': nome_prato, 'preco': preco, 'quantidade': 1}
                
                total += preco
                print(f"{nome_prato} adicionado ao pedido.")
            else:
                print("Código inválido. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    if not pedido:
        print("Nenhum prato foi selecionado.")
        return
    
    print("\nFormas de pagamento:")
    print("1 - À vista (10% de desconto)")
    print("2 - Cartão de crédito (10% de acréscimo)")
    
    while True:
        try:
            opcao_pagamento = int(input("Escolha a forma de pagamento: "))
            
            match opcao_pagamento:
                case 1:
                    desconto = total * 0.10
                    total_final = total - desconto
                    forma_pagamento = "À vista"
                case 2:
                    acrescimo = total * 0.10
                    total_final = total + acrescimo
                    forma_pagamento = "Cartão de crédito"
                case _:
                    print("Opção inválida. Escolha 1 ou 2.")
                    continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    print("\nResumo do Pedido:")
    for codigo, dados in pedido.items():
        print(f"{codigo} - {dados['nome']} - {dados['quantidade']}x R$ {dados['preco']:.2f}")
    print(f"Subtotal: R$ {total:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor final a ser pago: R$ {total_final:.2f}")

if __name__ == "__main__":
    main()
