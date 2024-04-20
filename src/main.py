def processar_entrada(nome_arquivo):
    """
    Lê o arquivo de entrada e armazena as informações do autômato em estruturas de dados adequadas.

    Args:
        nome_arquivo (str): Nome do arquivo de entrada.

    Returns:
        tuple: Tupla contendo os estados, símbolos, estados de aceitação e transições do autômato.
    """
    with open(nome_arquivo, 'r') as f:
        # Lê o número de estados
        num_estados = int(f.readline().strip())

        # Lê os símbolos terminais
        simbolos = f.readline().strip().split(' ')

        # Lê os estados de aceitação
        estados_aceitacao_line = f.readline().strip().split(' ')
        num_estados_aceitacao = int(estados_aceitacao_line[0])
        estados_aceitacao = [int(x) for x in estados_aceitacao_line[1:]]

        # Lê o número de transições
        num_transicoes = int(f.readline().strip())

        # Lê as transições
        transicoes = []
        for _ in range(num_transicoes):
            linha = f.readline().strip().split(' ')
            estado_inicial = int(linha[0])
            simbolo = linha[1]
            estado_final = int(linha[2])
            transicoes.append((estado_inicial, simbolo, estado_final))

        # Lê o número de cadeias de entrada
        num_cadeias_entrada = int(f.readline().strip())

        # Lê as cadeias de entrada
        cadeias_entrada = []
        for _ in range(num_cadeias_entrada):
            cadeias_entrada.append(f.readline().strip())

        print("Número de estados:", num_estados)
        print("Símbolos terminais:", simbolos)
        print("Estados de aceitação:", estados_aceitacao)
        print("Número de transições:", num_transicoes)
        print("Transições:", transicoes)
        print("Número de cadeias de entrada:", num_cadeias_entrada)
        print("Cadeias de entrada:", cadeias_entrada)

    return num_estados, simbolos, estados_aceitacao, transicoes, cadeias_entrada




def simular_automato(estados, simbolos, estados_aceitacao, transicoes, cadeia_entrada):
    """
    Simula a execução do autômato para uma cadeia de entrada específica.

    Args:
        estados (list): Lista de estados do autômato.
        simbolos (list): Lista de símbolos terminais do autômato.
        estados_aceitacao (list): Lista de estados de aceitação do autômato.
        transicoes (list): Lista de transições do autômato.
        cadeia_entrada (str): Cadeia de entrada a ser simulada.

    Returns:
        bool: True se a cadeia de entrada for aceita, False caso contrário.
    """
    print("\nCadeia atual:", cadeia_entrada)  # Imprime os estados iniciais
    
    estados_atuais = {estados[0]}  # Começa no estado inicial

    print("Estado atual:", estados_atuais)  # Imprime os estados iniciais

    for simbolo in cadeia_entrada:
        proximos_estados = set()
        print("Simbolo atual:", simbolo)  # Imprime o símbolo atual
        for estado in estados_atuais:
            # Encontra todas as transições possíveis para o símbolo atual e estado atual
            for estado_inicial, simbolo_transicao, estado_final in transicoes:
                if estado_inicial == estado and (simbolo_transicao == simbolo or simbolo_transicao == '-'):
                    proximos_estados.add(estado_final)
                    print("Transição encontrada:", estado_inicial, simbolo_transicao, estado_final)  # Imprime as transições encontradas
        estados_atuais = proximos_estados
        print("Estados atuais após o símbolo", simbolo, ":", estados_atuais)  # Imprime os estados atuais após o processamento do símbolo

    # Verifica se algum dos estados finais é um estado de aceitação
    resultado = any(estado_final in estados_aceitacao for _, _, estado_final in transicoes)

    print("Resultado da simulação:", resultado)  # Imprime o resultado da simulação
    return resultado


def gerar_saida(resultados, nome_arquivo):
    """
    Gera o arquivo de saída com os resultados da simulação.

    Args:
        resultados (list): Lista de resultados da simulação (True para aceita, False para rejeitada).
        nome_arquivo (str): Nome do arquivo de saída.
    """
    with open(nome_arquivo, 'w') as f:
        for resultado in resultados:
            if resultado:
                f.write("aceita\n")
            else:
                f.write("rejeita\n")


if __name__ == '__main__':
    # Lê as informações do autômato a partir do arquivo de entrada
    num_estados, simbolos, estados_aceitacao, transicoes, cadeias_entrada = processar_entrada('input.txt')

    # Simula a execução do autômato para cada cadeia de entrada
    resultados = []
    for cadeia_entrada in cadeias_entrada:
        resultado = simular_automato(list(range(num_estados)), simbolos, estados_aceitacao, transicoes, cadeia_entrada)
        resultados.append(resultado)

    # Gera o arquivo de saída com os resultados da simulação
    gerar_saida(resultados, 'output.txt')
