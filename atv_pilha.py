def novoLivro():
    titulo = input("Qual o titulo do livro?: ")
    autor = input("Qual seu autor?: ")
    paginas = int(input("Número de paginas do livro: "))
    return {
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
    }

def adicionarLivro(pilha):
    livro = novoLivro()
    pilha.append(livro)
    print("Livro empilhado! :D!")

def retirarLivro(pilha):
    if not pilha:
        print("Não há livros! :C")
        return None
    livro_retirado = pilha.pop()
    print(f"O livro {livro_retirado['titulo']} foi retirado da pilha!")

def printPilhaLivros(pilha):
    if not pilha:
        print("Não há livros! :C")
        return
    print("Livros empilhados:")
    for livro in reversed(pilha):
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Páginas: {livro["paginas"]}')

def menu():
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Retirar livro da pilha")
    print("3. Exibir livros empilhados")
    print("4. Sair")

def escolha(opcao, pilha):
    if opcao == '1':
        adicionarLivro(pilha)
    elif opcao == '2':
        retirarLivro(pilha)
    elif opcao == '3':
        printPilhaLivros(pilha)
    elif opcao == '4':
        return False
    else:
        print("Inválido")
    return True

def menu2():
    pilha_de_livros = []
    while True:
        menu()
        opcao = input("Escolha:")
        if not escolha(opcao, pilha_de_livros):
            break

menu2()
