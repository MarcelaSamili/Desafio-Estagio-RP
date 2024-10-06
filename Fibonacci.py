# Função para gerar a sequência de Fibonacci até o limite que a pessoa escolheu
limit = int(input('Quantos termos você deseja na sua sequência:'))
def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        print('{} -'.format(next_value), end=' ')
        sequence.append(next_value)
    return sequence

# Função para verificar se o número informado pertence à sequência de Fibonacci
def is_fibonacci(number):
    if number < 0:
        return False
    sequence = fibonacci_sequence(number)
    return number in sequence

# Número a ser verificado (pode ser alterado ou inserido por input)
num_to_check = int(input("Informe um número para que eu possa verificar se pertence à nossa sequência de Fibonacci: "))

# Verificação e exibição do resultado
if is_fibonacci(num_to_check):
    print(f"O número {num_to_check} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num_to_check} NÃO pertence à a nossa sequência de Fibonacci.")
    
  