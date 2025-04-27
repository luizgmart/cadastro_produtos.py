produtos = []


def cadastrar_produto():
    nome = input("Nome do Produto: ")
    descricao = input("Descrição do Produto: ")
    valor = input("Valor do Produto: ")

    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido. O produto não será cadastrado.")
        return

    disponivel = input("Disponível para venda (sim/não): ").strip().lower()
    if disponivel not in ['sim', 'não']:
        print("Opção inválida. O produto não será cadastrado.")
        return

    produto = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor,
        "disponivel": disponivel
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def exibir_listagem():
    if not produtos:
        print("Não há produtos cadastrados.")
        return

    # Ordena os produtos por valor (do menor para o maior)
    produtos_ordenados = sorted(produtos, key=lambda p: p['valor'])

    print("\nLista de Produtos Cadastrados:")
    print("Nome | Valor")
    for produto in produtos_ordenados:
        print(f"{produto['nome']} | R$ {produto['valor']:.2f}")


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Novo Produto")
        print("2. Exibir Listagem de Produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            exibir_listagem()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")



menu()