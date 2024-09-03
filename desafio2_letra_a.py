def count_letter_a(text):
    count = text.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

def desafio2_letra_a():
    texto = input("Informe uma string: ")  # Pode ser uma string pré-definida ou entrada do usuário
    resultado = count_letter_a(texto)
    print(resultado)
