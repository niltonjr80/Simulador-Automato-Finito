import collections

def process_input(filename):
    """
    Lê o arquivo de entrada e armazena as informações do autômato em estruturas de dados adequadas.

    Args:
        filename (str): Nome do arquivo de entrada.

    Returns:
        tuple: Tupla contendo os estados, símbolos, estados de aceitação e transições do autômato.
    """
    with open(filename, 'r') as f:
        # Lê o número de estados
        num_states = int(f.readline().strip())

        # Lê os símbolos terminais
        symbols = f.readline().strip().split(' ')

        # Lê os estados de aceitação
        accepting_states = [int(x) for x in f.readline().strip().split(' ')]

        # Lê o número de transições
        num_transitions = int(f.readline().strip())

        # Lê as transições
        transitions = []
        for _ in range(num_transitions):
            line = f.readline().strip().split(' ')
            start_state = int(line[0])
            end_state = int(line[1])
            symbol = line[2]
            transitions.append((start_state, end_state, symbol))

        # Lê o número de cadeias de entrada
        num_input_strings = int(f.readline().strip())

        # Lê as cadeias de entrada
        input_strings = []
        for _ in range(num_input_strings):
            input_strings.append(f.readline().strip())

    return num_states, symbols, accepting_states, transitions, input_strings


def simulate(states, symbols, accepting_states, transitions, input_string):
    """
    Simula a execução do autômato para uma cadeia de entrada específica.

    Args:
        states (list): Lista de estados do autômato.
        symbols (list): Lista de símbolos terminais do autômato.
        accepting_states (list): Lista de estados de aceitação do autômato.
        transitions (list): Lista de transições do autômato.
        input_string (str): Cadeia de entrada a ser simulada.

    Returns:
        bool: True se a cadeia de entrada for aceita, False caso contrário.
    """
    current_state = 0

    for symbol in input_string:
        # Verifica se existe transição para o símbolo atual
        found = False
        for start_state, end_state, transition_symbol in transitions:
            if start_state == current_state and (transition_symbol == symbol or transition_symbol == '-'):
                current_state = end_state
                found = True
                break

        if not found:
            return False

    # Verifica se o estado final é um estado de aceitação
    return current_state in accepting_states


def generate_output(input_strings, results, filename):
    """
    Gera o arquivo de saída com os resultados da simulação.

    Args:
        input_strings (list): Lista de cadeias de entrada.
        results (list): Lista de resultados da simulação (True para aceito, False para rejeitado).
        filename (str): Nome do arquivo de saída.
    """
    with open(filename, 'w') as f:
        for input_string, result in zip(input_strings, results):
            if result:
                f.write(f"{input_string}: aceita\n")
            else:
                f.write(f"{input_string}: rejeita\n")


if __name__ == '__main__':
    # Lê as informações do autômato a partir do arquivo de entrada
    num_states, symbols, accepting_states, transitions, input_strings = process_input('input.txt')

    # Simula a execução do autômato para cada cadeia de entrada
    results = []
    for input_string in input_strings:
        result = simulate(num_states, symbols, accepting_states, transitions, input_string)
        results.append(result)

    # Gera o arquivo de saída com os resultados da simulação
    generate_output(input_strings, results, 'output.txt')
