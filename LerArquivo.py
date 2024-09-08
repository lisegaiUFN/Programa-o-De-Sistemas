def ler_arquivo_para_string(caminho_arquivo):
    """
    Lê o conteúdo de um arquivo de texto e o retorna como uma string.
    
    Parâmetros:
    caminho_arquivo (str): Caminho do arquivo de texto.
    
    Retorna:
    str: Conteúdo do arquivo em uma única string.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Erro: {str(e)}"

def main():
    caminho = input("Digite o caminho do arquivo de texto: ")
    texto = ler_arquivo_para_string(caminho)
    print("\nConteúdo do arquivo transcrito para string:")
    print(texto)

if __name__ == "__main__":
    main()
