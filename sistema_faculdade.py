alunos = []
contador_matriculas = {}  


def cadastrar_aluno():
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ")
    email = input("E-mail: ")
    curso = input("Curso (ex: GES, GEC, GEA): ").upper()
    matricula = input("Matrícula: ")

    aluno = {"nome": nome, "email": email, "curso": curso, "matricula": matricula}
    alunos.append(aluno)

    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

def atualizar_aluno():
    print("\n--- Atualizar Aluno ---")
    matricula = input("Digite a matrícula do aluno a ser atualizado: ").upper()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: {aluno['nome']} ({aluno['matricula']})")
            aluno["nome"] = input("Novo nome: ") or aluno["nome"]
            aluno["email"] = input("Novo e-mail: ") or aluno["email"]
            aluno["curso"] = input("Novo curso (ex: GES, GEC, GEA): ").upper() or aluno["curso"]
            print("Aluno atualizado com sucesso!")
            return

    print("Aluno não encontrado.")

def remover_aluno():
    print("\n--- Remover Aluno ---")
    matricula = input("Digite a matrícula do aluno a ser removido: ").upper()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return

    print("Aluno não encontrado.")

def main():
    while True:
        print("\n===== Sistema da Faculdade =====")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
