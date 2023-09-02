# Paulo Henrique Perin
# Leonardo Lengler
# Davi Biscaia




def realizar_operacao(operacao, conjunto1, conjunto2, conjunto3=None):
  if operacao == 'U':
    resultado = conjunto1.union(conjunto2)
    operacao_descricao = 'União'
  elif operacao == 'I':
    resultado = conjunto1.intersection(conjunto2)
    operacao_descricao = 'Interseção'
  elif operacao == 'D':
    resultado1 = conjunto1.difference(conjunto2)
    resultado2 = conjunto2.difference(conjunto1)
    resultado = resultado1.union(resultado2)
    operacao_descricao = 'Diferença'
  elif operacao == 'C' and conjunto3 is not None:
    resultado = {(x, y, z) for x in conjunto1 for y in conjunto2 for z in conjunto3}
    operacao_descricao = 'Produto Cartesiano'
  else:
    return None

  if conjunto3 is None:
    return f"{operacao_descricao}: conjunto 1 ({', '.join(map(str, conjunto1))}), conjunto 2 ({', '.join(map(str, conjunto2))}). Resultado: {resultado}"
  else:
    return f"{operacao_descricao}: conjunto 1 ({', '.join(map(str, conjunto1))}), conjunto 2 ({', '.join(map(str, conjunto2))}), conjunto 3 ({', '.join(map(str, conjunto3))}). Resultado: {resultado}"



def main():
    try:
        nome_arquivo = input("Digite o nome do arquivo de entrada: ")
        with open(nome_arquivo, 'r') as arquivo:
            numero_de_operacoes = int(arquivo.readline().strip())
            for _ in range(numero_de_operacoes):
                operacao = arquivo.readline().strip()
                conjunto1 = set(arquivo.readline().strip().split(', '))
                conjunto2 = set(arquivo.readline().strip().split(', '))

                resultado = realizar_operacao(operacao, conjunto1, conjunto2)
                if resultado:
                    print(resultado)
                else:
                    print(f"Operação inválida: {operacao}")

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
