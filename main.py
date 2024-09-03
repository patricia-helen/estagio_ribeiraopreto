import desafio1_fibonacci
import desafio2_letra_a
import desafio3_soma
import desafio4_sequencias
import desafio5_interruptores

def main():
    while True:
        print("\nSelecione um desafio para executar:")
        print("1. Sequência de Fibonacci")
        print("2. Verificação de Letra 'a' em String")
        print("3. Valor Final de Variável em Código")
        print("4. Completar Sequências Numéricas")
        print("5. Problema dos Interruptores e Lâmpadas")
        print("6. Sair")

        escolha = input("Digite o número do desafio que deseja executar: ")

        if escolha == "1":
            desafio1_fibonacci.desafio1_fibonacci()
        elif escolha == "2":
            desafio2_letra_a.desafio2_letra_a()
        elif escolha == "3":
            desafio3_soma.desafio3_soma()
        elif escolha == "4":
            desafio4_sequencias.desafio4_sequencias()
        elif escolha == "5":
            desafio5_interruptores.desafio5_interruptores()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
