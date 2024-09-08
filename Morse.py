# Dicionário contendo as letras do alfabeto e seus equivalentes em Morse

ALFABETO_PARA_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# Invertendo o dicionário para permitir tradução de Morse para alfabeto
MORSE_PARA_ALFABETO = {valor: chave for chave, valor in ALFABETO_PARA_MORSE.items()}

def texto_para_morse(texto):
    """
    Traduz um texto do alfabeto para código Morse. 
    Cada letra é separada por um espaço no resultado.
    """
    morse = []
    for letra in texto.upper():
        if letra in ALFABETO_PARA_MORSE:
            morse.append(ALFABETO_PARA_MORSE[letra])
        else:
            morse.append('')  # Espaço para caracteres desconhecidos
    return ' '.join(morse)

def morse_para_texto(morse):
    """
    Traduz uma string em código Morse para o alfabeto.
    As palavras em Morse são separadas por espaços.
    """
    letras = morse.split(' ')
    texto = []
    for simbolo in letras:
        if simbolo in MORSE_PARA_ALFABETO:
            texto.append(MORSE_PARA_ALFABETO[simbolo])
        else:
            texto.append('')  # Espaço para caracteres desconhecidos
    return ''.join(texto)

def main():
    """
    Função principal que pergunta ao usuário o que ele deseja fazer
    e realiza a tradução de acordo com a escolha.
    """
    while True:
        print("\nEscolha uma opção:")
        print("1. Traduzir de alfabeto para Morse")
        print("2. Traduzir de Morse para alfabeto")
        print("3. Sair")
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == '1':
            texto = input("Digite uma palavra ou frase em alfabeto: ")
            print(f"Tradução para Morse: {texto_para_morse(texto)}")
        
        elif escolha == '2':
            morse = input("Digite uma palavra ou frase em Morse (letras separadas por espaços): ")
            print(f"Tradução para alfabeto: {morse_para_texto(morse)}")
        
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    